import os
import getpass
import time
import datetime
import shutil
import glob
import string
import re
import hashlib
import timeago

import kabaret.app.resources as resources
from kabaret import flow
from kabaret.flow_contextual_dict import ContextualView, get_contextual_dict
from kabaret.subprocess_manager.flow import RunAction

from .maputils import SimpleCreateAction, ClearMapAction

from .site import SyncMap, Request
from .runners import LaunchSessionWorker

class RevisionsChoiceValue(flow.values.ChoiceValue):

    STRICT_CHOICES = False

    _file = flow.Parent(2)

    def choices(self):
        return self._file.get_revisions().mapped_names()

    def revert_to_default(self):
        name = self._file.current_user_sees.get()
        if name == "current":
            if not self._file.has_current_revision():
                revisions = self._file.get_revisions().mapped_items()
                name = revisions[0].name()
            else:
                name = self._file.current_revision.get()

        self.set(name)


class CreateWorkingCopyFromRevision(flow.Action):

    _revision = flow.Parent()

    def get_buttons(self):
        msg = "<h3>Create a working copy</h3>"

        if self._revision._file.has_working_copy(from_current_user=True):
            msg += "<font color=#D66700>WARNING: You already have a working copy to your name. \
                    Choosing to create a new one will overwrite your changes.</font>"
        self.message.set(msg)

        return ["Create", "Cancel"]

    def needs_dialog(self):
        return self._revision._file.has_working_copy(from_current_user=True)

    def run(self, button):
        if button == "Cancel":
            return

        file = self._revision._file
        working_copy = file.create_working_copy(reference_name=self._revision.name())
        file.set_current_user_on_revision(working_copy.name())
        file.touch()
        file.get_revisions().touch()


class MakeCurrentRevisionAction(flow.Action):

    _revision = flow.Parent()

    def needs_dialog(self):
        return False

    def run(self, button):
        file = self._revision._file
        file.make_current(self._revision)
        file.get_revisions().touch()
        file.touch()


class OpenRevision(RunAction):
    _revision = flow.Parent()

    def needs_dialog(self):
        return False
    
    def extra_argv(self):
        return [self._revision.get_path()]
    
    def runner_name_and_tags(self):
        default_runners = self.root().project().admin.default_applications
        runner = default_runners[self._revision._file.format.get()]
        
        return runner.runner_name.get(), []


class ComputeRevisionHash(LaunchSessionWorker):
    _revision = flow.Parent()

    def allow_context(self, context):
        return False

    def launcher_oid(self):
        return self._revision.oid()

    def launcher_exec_func_name(self):
        return "update_hash"


class CheckRevisionHash(flow.Action):
    _revision = flow.Parent()

    def get_buttons(self):
        self.message.revert_to_default()
        return ["Check", "Close"]
    
    def run(self, button):
        if button == "Close":
            return

        if self._revision.hash_is_valid():
            color = "029600"
            msg = "Hash is valid !"
        else:
            color = "D5000D"
            msg = "Invalid hash"

        self.message.set((
            f"<h3><font color=#{color}>"
            f"{msg}</font></h3>"
        ))

        return self.get_result(close=False)


class Revision(flow.Object):

    _revisions = flow.Parent()
    _file = flow.Parent(3)

    user = flow.Param().ui(editable=False)
    date = flow.IntParam().ui(editable=False, editor="datetime")
    comment = flow.Param("").ui(editable=False)
    path = flow.Computed(cached=True)
    file_name = flow.Computed()
    hash = flow.Param("").ui(editable=False)

    site = flow.Param()
    sync = flow.Child(SyncMap).ui(expanded=True)

    open = flow.Child(OpenRevision)
    make_current = flow.Child(MakeCurrentRevisionAction)
    create_working_copy = flow.Child(CreateWorkingCopyFromRevision)
    request = flow.Child(Request)
    compute_hash_action = flow.Child(ComputeRevisionHash)
    check_hash = flow.Child(CheckRevisionHash)

    def get_path(self):
        return os.path.join(self.path.get(), self.file_name.get())
    
    def get_relative_path(self):
        return os.path.join(
            self._file.path.get(),
            self.name(),
            self.file_name.get()
        )

    def is_current(self):
        return self.name() == self._file.current_revision.get()

    def is_working_copy(self, from_current_user=False):
        if from_current_user:
            return self.name() == self.root().project().get_user()

        return self.name() == self.user.get()

    def get_sync_status(self, site_name=None):
        """
        Returns revision's status on the site identified
        by the given name.

        If site_name is None, this method returns its status
        on the current site.
        """
        if not site_name:
            site_name = self.root().project().admin.current_site_name.get()
        return self.sync[site_name].status.get()

    def set_sync_status(self, status, site_name=None):
        """
        Sets revision's status on the site identified
        by the given name to the given status.

        If site_name is None, this method sets its status
        on the current site.
        """
        if not site_name:
            site_name = self.root().project().admin.current_site_name.get()
        self.sync[site_name].status.set(status)

    def get_last_edit_time(self):
        if self.exists():
            return os.path.getmtime(self.get_path())
        
        return 0
    
    def exists(self):
        return os.path.exists(self.get_path())
    
    def compute_hash(self):
        path = self.get_path()
        
        if os.path.exists(path):
            with open(path, "rb") as f:
                content = f.read()

            return hashlib.md5(content).hexdigest()
    
    def update_hash(self):
        self.hash.set(self.compute_hash())
        self.hash.touch()
    
    def hash_is_valid(self):
        return self.hash.get() == self.compute_hash()

    def compute_child_value(self, child_value):
        if child_value is self.is_current:
            child_value.set(self.name() == self._file.current_revision.get())
        elif child_value is self.path:
            path = os.path.join(
                self.root().project().get_root("UNKNOWN_ROOT_DIR"),
                self._file.path.get(),
                self.name(),
            )
            child_value.set(path)
        elif child_value is self.file_name:
            name = "{filename}_{revision}.{ext}".format(
                filename=self._file.complete_name.get(),
                revision=self.name(),
                ext=self._file.format.get(),
            )
            child_value.set(name)


class ToggleSyncStatuses(flow.Action):
    _revisions = flow.Parent()

    def needs_dialog(self):
        return False
    
    def run(self, button):
        self._revisions._show_sync_statuses.set(
            not self._revisions._show_sync_statuses.get()
        )
        self._revisions.touch()


class ToggleShortNames(flow.Action):
    _revisions = flow.Parent()

    def needs_dialog(self):
        return False
    
    def run(self, button):
        self._revisions._enable_short_names.set(
            not self._revisions._enable_short_names.get()
        )
        self._revisions.touch()


class Revisions(flow.Map):

    _file = flow.Parent(2)
    _show_sync_statuses = flow.BoolParam(False)
    _enable_short_names = flow.BoolParam(False)

    toggle_sync_statuses = flow.Child(ToggleSyncStatuses)
    toggle_short_names = flow.Child(ToggleShortNames)

    @classmethod
    def mapped_type(cls):
        return Revision

    def columns(self):
        columns = ["Revision", "Created by", "On"]
        
        if self._show_sync_statuses.get():
            if self._enable_short_names.get():
                columns += self.root().project().admin.sites.short_names()
            else:
                columns += self.root().project().admin.sites.mapped_names()
        columns.append("Comment")

        return columns

    def add(self, name=None, object_type=None):
        publication_count = sum(
            list(map(lambda rev: int(not rev.is_working_copy()), self.mapped_items()))
        )

        if not name:
            name = "v{:03d}".format(publication_count + 1)

        rev = super(Revisions, self).add(name, object_type)
        rev.user.set(self.root().project().get_user())
        rev.date.set(time.time())
        rev.site.set(self.root().project().get_current_site().name())

        return rev

    def _fill_row_cells(self, row, item):
        item_name = item.name()
        if item.is_working_copy():
            item_name += " ("
            if item.is_working_copy(from_current_user=True):
                item_name += "your "
            item_name += "working copy)"
        
        if item.get_sync_status() == "Requested":
            item_name += " ⏳"

        row.update(
            {
                "Revision": item_name,
                "Created by": item.user.get(),
                "On": datetime.datetime.fromtimestamp(item.date.get()).ctime(),
                "Comment": item.comment.get(),
            }
        )

        if self._show_sync_statuses.get():
            if self._enable_short_names.get():
                names = self.root().project().admin.sites.short_names()
            else:
                names = self.root().project().admin.sites.mapped_names()
            
            d = dict.fromkeys(names, "")
            row.update(d)

    def _fill_row_style(self, style, item, row):
        seen_name = self._file.current_user_sees.get()
        if item.is_current():
            if item.name() == seen_name or seen_name == "current":
                style["icon"] = ('icons.libreflow', 'circular-shape-right-eye-silhouette')
            else:
                style["icon"] = ('icons.libreflow', 'circular-shape-silhouette')
        else:
            if item.name() == seen_name:
                style["icon"] = ('icons.libreflow', 'circle-shape-right-eye-outline')
            else:
                style["icon"] = ('icons.libreflow', 'circle-shape-outline')

        color_and_icon_by_status = {
            "Available": ("#45cc3d", ("icons.libreflow", "checked-symbol-colored")),
            "Requested": ("#cc3b3c", ("icons.libreflow", "exclamation-sign-colored")),
            "NotAvailable": ("#cc3b3c", ("icons.libreflow", "blank"))
        }
        style["foreground-color"] = color_and_icon_by_status[item.get_sync_status()][0]

        if self._show_sync_statuses.get():
            for s in item.sync.mapped_items():
                site_name = s.get_short_name() if self._enable_short_names.get() else s.name()
                style["%s_icon" % site_name] = color_and_icon_by_status[s.status.get()][1]
        
        style["Revision_activate_oid"] = item.open.oid()


class History(flow.Object):

    revisions = flow.Child(Revisions).injectable().ui(expanded=True)
    department = flow.Parent(3)


class FileFormat(flow.values.ChoiceValue):

    CHOICES = ["blend", "kra", "png", "jpg", "txt", "abc", "mov", "psd", "aep"]


class CreateTrackedFileAction(flow.Action):

    ICON = ("icons.gui", "plus-sign-in-a-black-circle")

    _files = flow.Parent()

    file_name = flow.Param("")
    file_format = flow.Param("blend", FileFormat).ui(
        choice_icons={
            "blend": ("icons.libreflow", "blender"),
            "kra": ("icons.libreflow", "krita"),
            "png": ("icons.gui", "picture"),
            "jpg": ("icons.gui", "picture"),
            "txt": ("icons.flow", "notepad"),
            "abc": ("icons.flow", "alembic"),
            "aep": ("icons.libreflow", "afterfx"),
            "psd": ("icons.flow", "photoshop"),
        }
    )

    def get_buttons(self):
        self.message.set("<h3>Create tracked file</h3>")
        return ["Create", "Cancel"]

    def run(self, button):
        if button == "Cancel":
            return

        settings = get_contextual_dict(self, "settings")
        file_category = settings.get("file_category", None)

        name = self.file_name.get()
        prefix = ""

        if file_category is not None:
            if file_category == "PROD":
                prefix = "{file_category}_{sequence}_{shot}_{department}_"
            elif file_category == "LIB":
                prefix = "{file_category}_{asset_name}_{department}_"

            prefix = prefix.format(**settings)

        self.root().session().log_debug(
            "Creating file %s.%s" % (name, self.file_format.get())
        )

        self._files.add_tracked_file(name, self.file_format.get(), prefix + name)
        self._files.touch()


class CreateWorkingCopyAction(flow.Action):

    _file = flow.Parent()

    from_revision = flow.Param(None, RevisionsChoiceValue).ui(label="Reference")

    def get_buttons(self):
        msg = "<h3>Create a working copy</h3>"

        if self._file.has_working_copy(from_current_user=True):
            msg += "<font color=#D66700>WARNING: You already have a working copy to your name. \
                    Choosing to create a new one will overwrite your changes.</font>"
        self.message.set(msg)

        if self._file.is_empty():
            self.from_revision.set("From scratch")
        else:
            self.from_revision.set(self._file.get_revisions().mapped_names()[0])

        return ["Create", "Create from scratch", "Cancel"]

    def needs_dialog(self):
        return not self._file.is_empty() or self._file.has_working_copy(
            from_current_user=True
        )

    def run(self, button):
        if button == "Cancel":
            return
        
        if button == "Create from scratch":
            working_copy = self._file.create_working_copy()
        else:
            ref_name = self.from_revision.get()

            if ref_name == "" or self._file.is_empty():
                ref_name = None
            elif not self._file.has_revision(ref_name):
                msg = self.message.get()
                msg += (
                    "<br><br><font color=#D5000D>There is no revision %s for this file.</font>"
                    % ref_name
                )
                self.message.set(msg)

                return self.get_result(close=False)

            working_copy = self._file.create_working_copy(reference_name=ref_name)

        self._file.set_current_user_on_revision(working_copy.name())
        self._file.touch()
        self._file.get_revisions().touch()


class GenericRunAction(RunAction):

    _file = flow.Parent()

    def runner_name_and_tags(self):
        ext = self._file.format.get()
        default_applications = self.root().project().admin.default_applications
        runner_name = default_applications[ext].runner_name.get()

        return runner_name, []

    def get_version(self, button):
        ext = self._file.format.get()
        default_applications = self.root().project().admin.default_applications
        runner_version = default_applications[ext].runner_version.get()

        return runner_version

    def get_buttons(self):
        ext = self._file.format.get()
        default_applications = self.root().project().admin.default_applications

        if not default_applications[ext].runner_name.get():
            self.message.set(
                "<h3>No default application for .%s file format.</h3>" % ext
            )
            return ["Cancel"]

        return super(GenericRunAction, self).get_buttons()

    def needs_dialog(self):
        ext = self._file.format.get()
        default_applications = self.root().project().admin.default_applications
        has_default_app = default_applications[ext].runner_name.get()

        return not has_default_app


class SeeRevisionAction(flow.Action):

    ICON = ("icons.libreflow", "watch")

    _file = flow.Parent()
    revision_name = flow.Param(None, RevisionsChoiceValue).ui(label="Revision")

    def get_buttons(self):
        self.message.set("<h3>Choose a revision to open</h3>")

        if self._file.is_empty():
            self.message.set("<h3>This file has no revision</h3>")
            return ["Cancel"]

        seen_name = self._file.current_user_sees.get()
        if seen_name != "current" or self._file.has_current_revision():
            if seen_name == "current":
                seen_name = self._file.current_revision.get()
            self.revision_name.set(seen_name)
        else:
            self.revision_name.set(self._file.get_revisions().mapped_names[0])

        return ["See", "Cancel"]

    def run(self, button):
        if button == "Cancel":
            return

        name = self.revision_name.get()

        if self._file.get_revision(name).is_current():
            name = "current"

        self._file.set_current_user_on_revision(name)
        self._file.touch()


class OpenFileAction(GenericRunAction):
    def extra_argv(self):
        return [self._file.get_path()]


class OpenTrackedFileAction(GenericRunAction):

    _to_open = flow.Param("")
    revision_name = flow.Param(None, RevisionsChoiceValue).ui(label="Revision")

    def get_buttons(self):
        if super(OpenTrackedFileAction, self).needs_dialog():
            return super(OpenTrackedFileAction, self).get_buttons()

        self.revision_name.revert_to_default()

        # At least one existing revision
        buttons = ["Open revision", "Cancel"]
        user_sees = self._file.current_user_sees.get()

        # Check if user's working copy already exists
        if not self._file.has_working_copy(from_current_user=True):
            buttons.insert(1, "Create a working copy")

        if user_sees == "current":
            if not self._file.has_current_revision():
                msg = "<h3>No active revision</h3>"
                # msg += "You aren't seeing any revision. Choose a revision to open, or create a working copy to edit."
                self.message.set(msg)
                self.revision_name.set(self._file.get_revisions().mapped_names()[0])

                return buttons

            user_sees = self._file.current_revision.get()

        # Current user is seeing a revision
        revision = self._file.get_revision(user_sees)
        self.revision_name.set(user_sees)

        if not revision.is_working_copy(from_current_user=True):
            msg = "<h3>Read-only mode</h3>"
            msg += "You're about to open this file in read-only mode. If you want to edit it, you can open your working copy or create one."
            self.message.set(msg)

        return buttons

    def needs_dialog(self):
        seen_name = self._file.current_user_sees.get()
        if seen_name == "current":
            seen = self._file.get_current_revision()
        else:
            seen = self._file.get_revision(seen_name)

        return not self._file.is_empty() and (
            seen is None or not seen.is_working_copy(from_current_user=True)
        )

    def extra_argv(self):
        revision = self._file.get_revision(self._to_open.get())
        return [revision.get_path()]

    def run(self, button):
        if button == "Cancel":
            return

        if button == "Create a working copy" or self._file.is_empty():
            ref_name = None if self._file.is_empty() else self.revision_name.get()
            working_copy = self._file.create_working_copy(reference_name=ref_name)
            revision_name = working_copy.name()
        elif button == "Open revision":
            revision_name = self.revision_name.get()
        else:
            revision_name = self._file.current_user_sees.get()

        self._file.set_current_user_on_revision(revision_name)
        self._to_open.set(revision_name)
        super(OpenTrackedFileAction, self).run(button)

        self._file.touch()


class OpenWithDefaultApp(RunAction):
    def runner_name_and_tags(self):
        return "DefaultEditor", []


class OpenWithAction(OpenTrackedFileAction):
    def runner_name_and_tags(self):
        raise NotImplementedError()

    def allow_context(self, context):
        return context and self._file.format.get() in self.supported_extensions()

    @classmethod
    def supported_extensions(cls):
        raise NotImplementedError()


class OpenWithBlenderAction(OpenWithAction):

    ICON = ("icons.libreflow", "blender")

    def runner_name_and_tags(self):
        return "Blender", []

    @classmethod
    def supported_extensions(cls):
        return ["blend"]


class OpenWithKritaAction(OpenWithAction):

    ICON = ("icons.libreflow", "krita")

    def runner_name_and_tags(self):
        return "Krita", []

    @classmethod
    def supported_extensions(cls):
        return ["kra", "png", "jpg"]


class OpenWithVSCodiumAction(OpenWithAction):

    ICON = ("icons.libreflow", "vscodium")

    def runner_name_and_tags(self):
        return "VSCodium", []

    @classmethod
    def supported_extensions(cls):
        return ["txt"]


class OpenWithNotepadPPAction(OpenWithAction):

    ICON = ("icons.flow", "notepad")

    def runner_name_and_tags(self):
        return "NotepadPP", []

    @classmethod
    def supported_extensions(cls):
        return ["txt"]


class PublishFileAction(LaunchSessionWorker):

    ICON = ("icons.libreflow", "publish")

    _file = flow.Parent()
    _department = flow.Parent(3)

    comment = flow.SessionParam("")
    upload_after_publish = flow.BoolParam(False)

    def get_buttons(self):
        self.message.set("<h3>Publish</h3>")

        if self._file.is_locked() and not self._file.is_locked(by_current_user=True):
            msg = "<h3>This file is already used by %s</h3>" % self._file.locked_by()
            msg += (
                "You can't publish your changes while the file is used by someone else."
            )
            self.message.set(msg)

            return ["Cancel"]

        return ["Keep editing", "Unlock", "Cancel"]

    def allow_context(self, context):
        return context and self._file.has_working_copy(True)
    
    def launcher_oid(self):
        return self.oid()

    def launcher_exec_func_name(self):
        return "upload_published_revision"
    
    def upload_published_revision(self):
        head = self._file.get_head_revision()
        current_site = self.root().project().get_current_site()

        upload_job = current_site.queue.submit_job(
            emitter_oid=head.oid(),
            user=self.root().project().get_user(),
            studio=current_site.name(),
            job_type='Upload',
            init_status='WAITING'
        )
        process_jobs_action = self.root().project().admin.process_jobs
        process_jobs_action._process(upload_job)

    def run(self, button):
        if button == "Cancel":
            return

        self._file.lock()
        keep_editing = button == "Keep editing"
        published_revision = self._file.publish(self.comment.get(), keep_editing)

        if not keep_editing:
            self._file.set_current_user_on_revision(published_revision.name())
            self._file.unlock()

        if self._department.auto_current.get():
            published_revision.make_current.run(None)

        self._file.touch()

        if self.upload_after_publish.get():
            super(PublishFileAction, self).run(None)


class MakeFileCurrentAction(flow.Action):

    _file = flow.Parent()

    def needs_dialog(self):
        return False

    def allow_context(self, context):
        head_revision = self._file.get_head_revision()
        return (
            context and head_revision is not None and not head_revision.is_current()
        )  # And user is admin ?

    def run(self, button):
        self.root().session().log_debug(
            "Make latest revision of file %s current" % self._file.name()
        )

        self._file.make_current(self._file.get_head_revision())
        self._file.touch()


class GotoHistory(flow.Action):

    ICON = ("icons.gui", "ui-layout")

    _file = flow.Parent()

    def needs_dialog(self):
        return False

    def run(self, button):
        return self.get_result(goto=self._file.history.oid())


class LockAction(flow.Action):

    ICON = ("icons.gui", "padlock")

    _file = flow.Parent()

    def get_buttons(self):
        if self._file.is_locked(by_current_user=True):
            msg = "<h2>You already locked this file.</h2>"
        else:
            msg = (
                "<h2>This file is already locked by <b>%s</b></h2>"
                % self._file.locked_by()
            )
        self.message.set(msg)

        return []

    def needs_dialog(self):
        return self._file.is_locked()

    def run(self, button):
        self._file.lock()
        self._file._map.touch()


class UnlockAction(flow.Action):

    ICON = ("icons.gui", "open-padlock-silhouette")

    _file = flow.Parent()

    def get_buttons(self):
        msg = (
            "<h2>This file is already locked by <b>%s</b></h2>\n"
            % self._file.locked_by()
        )
        msg += "You can't unlock a file locked by another user."
        self.message.set(msg)

        return ["Cancel"]

    def needs_dialog(self):
        current_user = self.root().project().get_user()
        is_admin = self.root().project().is_admin(current_user)

        return (
            self._file.is_locked()
            and not self._file.is_locked(by_current_user=True)
            and not is_admin
        )

    def run(self, button):
        if button == "Cancel":
            return

        self._file.unlock()
        self._file._map.touch()


class UserSees(flow.values.Value):
    pass


class ActiveUsers(flow.Map):
    @classmethod
    def mapped_type(cls):
        return UserSees

    def columns(self):
        return ["User", "Revision"]

    def _fill_row_cells(self, row, item):
        row["User"] = item.name()
        row["Revision"] = item.get()


class FileSystemItem(flow.Object):

    _department = flow.Parent(2)
    settings = flow.Child(ContextualView).ui(hidden=True)
    path = flow.Computed(cached=True)

    def get_name(self):
        return self.name()

    def get_path(self):
        return os.path.join(
            self.root().project().get_root(),
            self.path.get()
        )

    def get_last_edit_time(self):
        path = self.get_path()
        if os.path.exists(path):
            return os.path.getmtime(path)
        
        return 0
    
    def compute_child_value(self, child_value):
        if child_value is self.path:
            child_value.set(os.path.join(
                self._department.path.get(),
                self.get_name()
            ))


class File(FileSystemItem):

    format = flow.Param("blend", FileFormat).ui(editable=False).injectable()
    display_name = flow.Computed()
    open = flow.Child(OpenFileAction)

    def get_name(self):
        return "%s.%s" % (self.name(), self.format.get())

    def get_template_path(self):
        try:
            return resources.get("file_templates", "template.%s" % self.format.get())
        except resources.NotFoundError:
            raise resources.NotFoundError(
                "No template file for '%s' format." % self.format.get()
            )

    def compute_child_value(self, child_value):
        if child_value is self.display_name:
            file_name = "_".join(self.name().split("_")[:-1])
            child_value.set("%s.%s" % (file_name, self.format.get()))
        else:
            super(File, self).compute_child_value(child_value)


class SearchExistingRevisions(flow.Action):

    _file = flow.Parent()

    def needs_dialog(self):
        return False

    def run(self, button):
        folders = [
            f for f in os.listdir(self._file.get_path()) if re.search(r"^v\d\d\d$", f)
        ]
        revisions = self._file.get_revisions()

        for name in folders:
            try:
                revisions.add(name)
            except ValueError:
                pass

        revisions.touch()


class TrackedFile(File):

    ICON = ("icons.gui", "text-file-1")

    _map = flow.Parent()
    _department = flow.Parent(2)
    _locked_by = flow.Param("")

    complete_name = flow.Param("").ui(editable=False)
    state = flow.Computed()

    history = flow.Child(History)
    current_revision = flow.Param("").ui(editable=False)

    active_users = flow.Child(ActiveUsers)
    current_user_sees = flow.Computed()

    show_history = flow.Child(GotoHistory)
    create_working_copy_action = flow.Child(CreateWorkingCopyAction).ui(
        label="Create working copy"
    )
    publish_action = flow.Child(PublishFileAction).ui(label="Publish")
    make_current_action = flow.Child(MakeFileCurrentAction).ui(
        label="Set last as current"
    )
    open = flow.Child(OpenTrackedFileAction)
    see_revision = flow.Child(SeeRevisionAction).ui(label="See revision...")
    lock_action = flow.Child(LockAction).ui(label="Lock")
    unlock_action = flow.Child(UnlockAction).ui(label="Unlock")
    search_existing_revisions = flow.Child(SearchExistingRevisions)

    with flow.group("Open with"):
        open_with_blender = flow.Child(OpenWithBlenderAction).ui(label="Blender")
        open_with_krita = flow.Child(OpenWithKritaAction).ui(label="Krita")
        open_with_vscodium = flow.Child(OpenWithVSCodiumAction).ui(label="VSCodium")
        open_with_notepadpp = flow.Child(OpenWithNotepadPPAction).ui(label="Notepad++")

    def get_name(self):
        return "%s_%s" % (self.complete_name.get(), self.format.get())

    def is_locked(self, by_current_user=False):
        if by_current_user:
            return self.locked_by() == self.root().project().get_user()

        return bool(self._locked_by.get())

    def locked_by(self):
        return self._locked_by.get()

    def lock(self):
        current_user = self.root().project().get_user()
        self._locked_by.set(current_user)

    def unlock(self):
        self._locked_by.set("")

    def has_working_copy(self, from_current_user=False):
        if from_current_user:
            user = self.root().project().get_user()
            return user in self.get_revisions().mapped_names()

        for revision in self.get_revisions().mapped_items():
            if revision.is_working_copy():
                return True

        return False

    def set_current_user_on_revision(self, revision_name):
        current_user = self.root().project().get_user()
        self.set_user_on_revision(current_user, revision_name)

    def set_user_on_revision(self, user_name, revision_name):
        if self.has_active_user(user_name):
            active_user = self.active_users[user_name]
        else:
            active_user = self.active_users.add(user_name)

        active_user.set(revision_name)
        self.get_revisions().touch()

    def remove_active_user(self, user_name):
        self.active_users.remove(user_name)

    def has_active_user(self, user_name):
        return user_name in self.active_users.mapped_names()

    def get_seen_revision(self):
        name = self.current_user_sees.get()

        if name == "current":
            if self.has_current_revision():
                return self.get_current_revision()
            else:
                return None
        else:
            return self.get_revision(name)

    def has_current_revision(self):
        return bool(self.current_revision.get())

    def get_revision(self, name):
        return self.history.revisions[name]

    def get_revisions(self):
        return self.history.revisions

    def has_revision(self, name):
        return name in self.history.revisions.mapped_names()

    def is_empty(self):
        return not bool(len(self.get_revisions()))

    def get_last_edit_time(self):
        seen_name = self.current_user_sees.get()
        current = self.get_current_revision()

        if seen_name == "current":
            if current is None:
                if os.path.exists(self.get_path()):
                    return os.path.getmtime(self.get_path())
                else:
                    return 0
            else:
                return current.get_last_edit_time()
        else:
            seen = self.get_revision(seen_name)
            return seen.get_last_edit_time()

    def get_last_comment(self):
        seen_name = self.current_user_sees.get()
        current = self.get_current_revision()

        if seen_name == "current":
            if current is None:
                return "NO PUBLISH YET"
            else:
                return current.comment.get()
        else:
            seen = self.get_revision(seen_name)

            if seen.is_working_copy():
                return "WORKING COPY (%s)" % seen.user.get()
            else:
                return seen.comment.get()

    def create_working_copy(self, reference_name=None, user_name=None):
        if user_name is None:
            user_name = self.root().project().get_user()

        revisions = self.get_revisions()

        enable_os = (
            self.root().project().admin.enable_filesystem_operations.get()
        )  # Lovely

        # Overwrite current working copy
        try:
            working_copy = revisions[user_name]
        except flow.exceptions.MappedNameError:
            # No working copy, will be created below
            pass
        else:
            if enable_os:
                try:
                    shutil.rmtree(working_copy.path.get())
                except FileNotFoundError:
                    self.root().session().log_warning(
                        "File '{}' no longer exists".format(working_copy.path.get())
                    )

            revisions.remove(user_name)

        working_copy = revisions.add(user_name)
        working_copy.set_sync_status("Available")

        if enable_os:
            try:
                os.makedirs(working_copy.path.get())
            except OSError:
                self.root().session().log_error(
                    "Creation of working copy folder '%s' failed\n\n==> TRACEBACK\n"
                    % working_copy.path.get()
                )
                raise

            working_copy_path = working_copy.get_path()

            if reference_name is None:
                # Create working copy from scratch
                file_path = self.get_template_path()
                self.root().session().log_debug(
                    "Copy template {} to {}".format(file_path, working_copy_path)
                )
            else:
                reference = self.get_revision(reference_name)
                file_path = reference.get_path()

                self.root().session().log_debug(
                    "Copy current revision {} to {}".format(
                        file_path, working_copy_path
                    )
                )

            try:
                shutil.copy2(file_path, working_copy_path)
            except OSError:
                self.root().session().log_error(
                    "Copy of template '{}' failed\n\n==> TRACEBACK\n".format(file_path)
                )
                raise

        return working_copy

    def publish(self, comment="", keep_editing=False):
        revisions = self.get_revisions()
        head_revision = revisions.add()
        head_revision.comment.set(comment)
        head_revision_path = head_revision.get_path()
        head_revision.set_sync_status("Available")
        working_copy = self.get_working_copy()
        working_copy_path = working_copy.get_path()

        enable_os = (
            self.root().project().admin.enable_filesystem_operations.get()
        )  # Lovely

        if enable_os:
            self.root().session().log_debug(
                "Create head revision folder {}".format(head_revision.path.get())
            )

            try:
                os.mkdir(head_revision.path.get())
            except OSError:
                self.root().session().log_error(
                    "Creation of head revision folder '{}' failed\n\n==> TRACEBACK\n".format(
                        head_revision.path.get()
                    )
                )
                raise

        if keep_editing:
            if enable_os:
                self.root().session().log_debug(
                    "Copy working copy {} to {}".format(
                        working_copy_path, head_revision_path
                    )
                )

                shutil.copy2(working_copy_path, head_revision_path)
        else:
            if enable_os:
                self.root().session().log_debug(
                    "Copy working copy {} to {}".format(
                        working_copy_path, head_revision_path
                    )
                )
                self.root().session().log_debug(
                    "Remove working copy folder {}".format(working_copy.path.get())
                )

                shutil.move(working_copy_path, head_revision_path)
                shutil.rmtree(working_copy.path.get())

            revisions.remove(working_copy.name())

        revisions.touch()

        # Compute published revision hash
        head_revision.compute_hash_action.run(None)

        return head_revision

    def make_current(self, revision):
        revision_path = os.path.join(revision.path.get(), revision.file_name.get())
        current_path, current_name = self.get_current_revision_params()
        current_revision_path = os.path.join(current_path, current_name)

        enable_os = (
            self.root().project().admin.enable_filesystem_operations.get()
        )  # Lovely

        if not os.path.exists(current_path):
            os.makedirs(current_path)

        if enable_os:
            try:
                # TODO: make it work
                self.root().session().log_debug(
                    "Create symlink {} pointing to {}".format(
                        revision.path.get(), current_path
                    )
                )
                os.symlink(revision.path.get(), current_path, target_is_directory=True)
            except OSError:
                self.root().session().log_warning("Symbolic link privilege not held...")

                try:
                    self.root().session().log_debug(
                        "Copy working copy {} to {}".format(
                            revision_path, current_revision_path
                        )
                    )
                    shutil.copy2(revision_path, current_revision_path)
                except OSError:
                    self.root().session().log_error(
                        "Copy of head revision '{}' to current failed".format(
                            revision_path
                        )
                    )
                    raise

        self.current_revision.set(revision.name())
        self.get_revisions().touch()

    def get_working_copy(self, user_name=None):
        if user_name is None:
            user_name = self.root().project().get_user()
        try:
            return self.get_revision(user_name)
        except flow.exceptions.MappedNameError:
            return None

    def get_head_revision(self):
        revisions = self.get_revisions()

        for revision in reversed(revisions.mapped_items()):
            if not revision.is_working_copy():
                return revision

        return None

    def get_current_revision(self):
        try:
            return self.get_revision(self.current_revision.get())
        except flow.exceptions.MappedNameError:
            return None

    def get_current_revision_params(self):
        revision_path = os.path.join(self.get_path(), "current")
        revision_name = "%s_current.%s" % (self.complete_name.get(), self.format.get())

        return revision_path, revision_name

    def compute_child_value(self, child_value):
        current_user = self.root().project().get_user()

        if child_value is self.current_user_sees:
            try:
                child_value.set(self.active_users[current_user].get())
            except flow.exceptions.MappedNameError:
                child_value.set("current")

        elif child_value is self.state:
            seen_name = self.current_user_sees.get()

            if seen_name == "current":
                if self.has_current_revision():
                    if self.get_head_revision().is_current():
                        child_value.set("<o>")
                    else:
                        child_value.set("o>")
                else:
                    if self.has_working_copy():
                        child_value.set("-o")
                    else:
                        child_value.set("--")
            else:
                seen = self.get_revision(seen_name)
                head = self.get_head_revision()
                current = self.get_current_revision()

                # Consider by default we're on our working copy more recent than the current
                child_value.set(">")

                if seen.is_working_copy(from_current_user=True):
                    if (
                        head is not None
                        and seen.get_last_edit_time() < head.get_last_edit_time()
                    ):
                        child_value.set("< !")
                    elif (
                        current is not None
                        and seen.get_last_edit_time() == current.get_last_edit_time()
                    ):
                        child_value.set("=")
                else:  # Read-only revision
                    if seen.is_working_copy():
                        # Seen working copy more recent than head by default
                        child_value.set("<o %s" % seen.name())

                        if head is None:
                            if seen.get_last_edit_time() < head.get_last_edit_time():
                                child_value.set("o> %s" % seen.name())
                            elif seen.get_last_edit_time() == head.get_last_edit_time():
                                child_value.set("<o> %s" % seen.name())
                    else:
                        child_value.set(
                            "<o %s" % seen.name()
                        )  # Seen publication more recent than current by default

                        if head is not None and current is not None:
                            if seen.get_last_edit_time() < head.get_last_edit_time():
                                child_value.set("o> %s" % seen.name())
                            elif (
                                seen.get_last_edit_time()
                                == current.get_last_edit_time()
                                and seen.get_last_edit_time()
                                == head.get_last_edit_time()
                            ):
                                child_value.set("<o> %s" % seen.name())
        else:
            super(TrackedFile, self).compute_child_value(child_value)


class ClearFileSystemMapAction(ClearMapAction):
    def run(self, button):
        for item in self._map.mapped_items():
            if hasattr(item, "state") and hasattr(item, "current_user_sees"):
                item.get_revisions().clear()
                item.current_revision.set("")
                item.active_users.clear()

        super(ClearFileSystemMapAction, self).run(button)


class OpenFolderAction(RunAction):

    _folder = flow.Parent()

    def runner_name_and_tags(self):
        return "DefaultEditor", []

    def extra_argv(self):
        return [os.path.normpath(self._folder.get_path())]

    def needs_dialog(self):
        return False


class CreateFileSystemItemAction(SimpleCreateAction):
    def get_buttons(self):
        self.message.set("<h2>Create %s</h2>" % self.item_type().__name__.lower())

        return ["Create", "Cancel"]

    @classmethod
    def item_type(cls):
        return FileSystemItem

    def _add_item(self, name):
        raise NotImplementedError(
            "Needs to be implemented by calling the proper add method in the FileSystemMap"
        )

    def run(self, button):
        if button == "Cancel":
            return

        if self.entity_name.get() == "":
            msg = self.message.get()
            msg += (
                "<font color=#D5000D>%s name must be not empty.</font>"
                % self.item_type().__name__
            )
            self.message.set(msg)

            return self.get_result(close=False)

        self._add_item(self.entity_name.get())
        self._map.touch()


class Folder(FileSystemItem):

    _department = flow.Parent(2)
    open = flow.Child(OpenFolderAction)


class TrackedFolder(Folder):
    # TODO
    pass


class CreateFileAction(CreateFileSystemItemAction):

    format = flow.Param("blend", FileFormat)

    @classmethod
    def item_type(cls):
        return File

    def _add_item(self, name):
        return self._map.add_file(name, self.format.get())


class CreateFolderAction(CreateFileSystemItemAction):
    @classmethod
    def item_type(cls):
        return Folder

    def _add_item(self, name):
        return self._map.add_folder(name)


class FileSystemMap(flow.Map):

    create_file = flow.Child(CreateTrackedFileAction).injectable()
    create_untracked_folder = flow.Child(CreateFolderAction)
    create_untracked_file = flow.Child(CreateFileAction)
    clear_map = flow.Child(ClearFileSystemMapAction).ui(hidden=True)

    @classmethod
    def mapped_type(cls):
        return FileSystemItem

    def columns(self):
        return ["Lock", "Name", "Last comment"]

    def _fill_row_cells(self, row, item):
        if isinstance(item, File):
            row["Name"] = item.display_name.get()
        else:
            row["Name"] = item.name()

        if hasattr(item, "state") and hasattr(item, "get_last_comment"):
            row["Lock"] = ""
            # row["State"] = item.state.get()
            row["Last comment"] = item.get_last_comment()
        else:
            row["Lock"] = "-"
            # row["State"] = "-"
            row["Last comment"] = "-"

        row['Last edit'] =  timeago.format(datetime.datetime.fromtimestamp(item.get_last_edit_time()), datetime.datetime.now())

    def _fill_row_style(self, style, item, row):
        style["icon"] = ("icons.libreflow", "blank")
        style["Name_icon"] = ("icons.gui", "folder-white-shape")

        if isinstance(item, TrackedFile) or isinstance(item, TrackedFolder):
            if item.is_locked():
                if item.is_locked(by_current_user=True):
                    style["icon"] = ("icons.libreflow", "padlock_green")
                else:
                    style["icon"] = ("icons.libreflow", "padlock_red")

        if isinstance(item, File):
            default_applications = self.root().project().admin.default_applications
            try:
                default_app = default_applications[item.format.get()]
            except flow.exceptions.MappedNameError:
                pass
            else:
                try:
                    style["Name_icon"] = default_app.get_runner().runner_icon()
                except AttributeError:
                    pass

        style["activate_oid"] = item.open.oid()

    def _parse_filename(self, filename, **params):
        formatted_name, extension = tuple(filename.split("."))

        # Remove arguments in file formatted_name not provided
        for _, arg, _, _ in string.Formatter().parse(formatted_name):
            if not arg in params:
                formatted_name.replace("{{arg}}".format(arg=arg), "")

        formatted_name.replace("__", "_")
        name = re.sub("{.*}", "", formatted_name)

        if name.startswith("_"):
            name = name[1:]
        if name.endswith("_"):
            name = name[:-1]

        name = re.sub("-", "_", name)
        complete_name = formatted_name.format(**params)

        return name, complete_name, extension

    def add_from_filename(self, filename, params=None, object_type=None):
        if params is None:
            params = {}

        name, complete_name, extension = self._parse_filename(filename, **params)

        file = self.add_tracked_file(name, extension, complete_name)
        file.unlock()

        return file

    def add_file(self, name, extension):
        key = "%s_%s" % (name, extension)
        file = self.add(key, object_type=File)
        file.format.set(extension)

        if self.root().project().admin.enable_filesystem_operations.get():
            # Create file's parent folder
            parent_folder = os.path.abspath(os.path.join(file.get_path(), ".."))
            try:
                os.makedirs(parent_folder)
            except OSError:
                # Folder already created
                pass

            # Create file from template
            try:
                shutil.copyfile(file.get_template_path(), file.get_path())
            except OSError:
                self.root().session().log_error(
                    "File %s already exists" % file.get_path()
                )
                raise

        return file

    def add_folder(self, name):
        folder = self.add(name, object_type=Folder)

        if self.root().project().admin.enable_filesystem_operations.get():
            try:
                if os.path.exists(folder.get_path()):
                    print("Folder %s already exists" % folder.get_path())
                else:
                    os.makedirs(folder.get_path())
            except OSError:
                self.root().session().log_error(
                    "Error while creating folder %s" % folder.get_path()
                )
                raise

        return folder

    def add_tracked_file(self, name, extension, complete_name):
        key = "%s_%s" % (name, extension)
        file = self.add(key, object_type=TrackedFile)
        file.format.set(extension)
        file.complete_name.set(complete_name)

        if self.root().project().admin.enable_filesystem_operations.get():
            # Create file folder
            try:
                self.root().session().log_debug(
                    "Create file folder '{}'".format(file.get_path())
                )
                os.makedirs(file.get_path())
            except OSError:
                self.root().session().log_error(
                    "Creation of file folder '{}' failed.".format(file.get_path())
                )
                pass

            # Create current revision folder
            current_revision_folder = os.path.join(file.get_path(), "current")

            try:
                self.root().session().log_debug(
                    "Create current revision folder '{}'".format(
                        current_revision_folder
                    )
                )
                os.mkdir(current_revision_folder)
            except OSError:
                self.root().session().log_error(
                    "Creation of current revision folder '{}' failed".format(
                        current_revision_folder
                    )
                )
                pass

        return file

    def add_tracked_folder(self, name, complete_name):
        raise NotImplementedError("Not implemented yet")

    def clear(self):
        if self.root().project().admin.enable_filesystem_operations.get():
            for item in self.mapped_items():
                try:
                    if type(item) is File:
                        os.remove(item.get_path())
                    else:
                        shutil.rmtree(item.get_path())
                except FileNotFoundError:
                    self.root().session().log_warning(
                        "%s %s no longer exists"
                        % (item.__class__.__name__, item.get_path())
                    )

        super(FileSystemMap, self).clear()
