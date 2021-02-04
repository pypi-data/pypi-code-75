# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reversion_compare']

package_data = \
{'': ['*'],
 'reversion_compare': ['locale/de/LC_MESSAGES/*',
                       'locale/el/LC_MESSAGES/*',
                       'locale/fi/LC_MESSAGES/*',
                       'locale/fr/LC_MESSAGES/*',
                       'locale/nl/LC_MESSAGES/*',
                       'locale/pl/LC_MESSAGES/*',
                       'templates/reversion-compare/*']}

install_requires = \
['diff-match-patch', 'django-reversion']

entry_points = \
{'console_scripts': ['publish = reversion_compare.publish:publish',
                     'run_testserver = '
                     'reversion_compare_tests.manage:start_test_server',
                     'update_rst_readme = '
                     'reversion_compare.publish:update_readme']}

setup_kwargs = {
    'name': 'django-reversion-compare',
    'version': '0.13.1',
    'description': 'history compare for django-reversion',
    'long_description': '========================\ndjango-reversion-compare\n========================\n\n**django-reversion-compare** is an extension to `django-reversion <https://github.com/etianen/django-reversion/>`_ that provides a history compare view to compare two versions of a model which is under reversion.\n\nComparing model versions is not a easy task. Maybe there are different view how this should looks like.\nThis project will gives you a generic way to see whats has been changed.\n\nMany parts are customizable by overwrite methods or subclassing, see above.\n\n+--------------------------------------+--------------------------------------------------------------------+\n| |Build Status on github|             | `github.com/jedie/django-reversion-compare/actions`_               |\n+--------------------------------------+--------------------------------------------------------------------+\n| |Coverage Status on coveralls.io|    | `coveralls.io/r/jedie/django-reversion-compare`_                   |\n+--------------------------------------+--------------------------------------------------------------------+\n| |Coverage Status on codecov.io|      | `codecov.io/gh/jedie/django-reversion-compare`_                    |\n+--------------------------------------+--------------------------------------------------------------------+\n| |Requirements Status on requires.io| | `requires.io/github/jedie/django-reversion-compare/requirements/`_ |\n+--------------------------------------+--------------------------------------------------------------------+\n\n.. |Build Status on github| image:: https://github.com/jedie/django-reversion-compare/workflows/test/badge.svg?branch=master\n.. _github.com/jedie/django-reversion-compare/actions: https://github.com/jedie/django-reversion-compare/actions\n.. |Coverage Status on coveralls.io| image:: https://coveralls.io/repos/jedie/django-reversion-compare/badge.svg\n.. _coveralls.io/r/jedie/django-reversion-compare: https://coveralls.io/r/jedie/django-reversion-compare\n.. |Coverage Status on codecov.io| image:: https://codecov.io/gh/jedie/django-reversion-compare/branch/master/graph/badge.svg\n.. _codecov.io/gh/jedie/django-reversion-compare: https://codecov.io/gh/jedie/django-reversion-compare\n.. |Requirements Status on requires.io| image:: https://requires.io/github/jedie/django-reversion-compare/requirements.svg\n.. _requires.io/github/jedie/django-reversion-compare/requirements/: https://requires.io/github/jedie/django-reversion-compare/requirements/\n\n------------\nInstallation\n------------\n\nJust use:\n\n::\n\n    pip install django-reversion-compare\n\nSetup\n=====\n\nAdd **reversion_compare** to **INSTALLED_APPS** in your settings.py, e.g.:\n\n::\n\n    INSTALLED_APPS = (\n        \'django...\',\n        ...\n        \'reversion\', # https://github.com/etianen/django-reversion\n        \'reversion_compare\', # https://github.com/jedie/django-reversion-compare\n        ...\n    )\n    \n    # Add reversion models to admin interface:\n    ADD_REVERSION_ADMIN=True\n    # optional settings:\n    REVERSION_COMPARE_FOREIGN_OBJECTS_AS_ID=False\n    REVERSION_COMPARE_IGNORE_NOT_REGISTERED=False\n\nUsage\n=====\n\nInherit from **CompareVersionAdmin** instead of **VersionAdmin** to get the comparison feature.\n\nadmin.py e.g.:\n\n::\n\n    from django.contrib import admin\n    from reversion_compare.admin import CompareVersionAdmin\n    \n    from my_app.models import ExampleModel\n    \n    @admin.register(ExampleModel)\n    class ExampleModelAdmin(CompareVersionAdmin):\n        pass\n\nIf you\'re using an existing third party app, then you can add patch django-reversion-compare into\nits admin class by using the **reversion_compare.helpers.patch_admin()** method. For example, to add\nversion control to the built-in User model:\n\n::\n\n    from reversion_compare.helpers import patch_admin\n    \n    patch_admin(User)\n\ne.g.: Add django-cms Page model:\n\n::\n\n    from cms.models.pagemodel import Page\n    from reversion_compare.helpers import patch_admin\n    \n    \n    # Patch django-cms Page Model to add reversion-compare functionality:\n    patch_admin(Page)\n\nCustomize\n=========\n\nIt\'s possible to change the look for every field or for a entire field type.\nYou must only define a methods to your admin class with this name scheme:\n\n*  ``"compare_%s" % field_name`` \n\n*  ``"compare_%s" % field.get_internal_type()`` \n\nIf there is no method with this name scheme, the ``fallback_compare()`` method will be used.\n\nAn example for specifying a compare method for a model field by name:\n\n::\n\n    class YourAdmin(CompareVersionAdmin):\n        def compare_foo_bar(self, obj_compare):\n            """ compare the foo_bar model field """\n            return "%r <-> %r" % (obj_compare.value1, obj_compare.value2)\n\nand example using **patch_admin** with custom version admin class:\n\n::\n\n    patch_admin(User, AdminClass=YourAdmin)\n\n----------------\nClass Based View\n----------------\n\nBeyond the Admin views, you can also create a Class Based View for displaying and comparing version\ndifferences. This is a single class-based-view that either displays the list of versions to select\nfor an object or displays both the versions **and** their differences (if the versions to be compared\nhave been selected). This class can be used just like a normal DetailView:\n\nMore information about this can be found in DocString of:\n\n* `https://github.com/jedie/django-reversion-compare/blob/master/reversion_compare/views.py <HistoryCompareDetailView>`_\n\nThe ``make run-test-server`` test project contains a Demo, use the links under:\n\n::\n\n    HistoryCompareDetailView Examples:\n\n-----------\nScreenshots\n-----------\n\nHere some screenshots of django-reversion-compare:\n\n----\n\nHow to select the versions to compare:\n\n|django-reversion-compare_v0_1_0-01.png|\n\n.. |django-reversion-compare_v0_1_0-01.png| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/django-reversion-compare/20120508_django-reversion-compare_v0_1_0-01.png\n\n----\n\nfrom **v0.1.0**: DateTimeField compare (last update), TextField compare (content) with small changes and a ForeignKey compare (child model instance was added):\n\n|django-reversion-compare_v0_1_0-02.png|\n\n.. |django-reversion-compare_v0_1_0-02.png| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/django-reversion-compare/20120508_django-reversion-compare_v0_1_0-02.png\n\n----\n\nfrom **v0.1.0**: Same as above, but the are more lines changed in TextField and the ForeignKey relation was removed:\n\n|django-reversion-compare_v0_1_0-03.png|\n\n.. |django-reversion-compare_v0_1_0-03.png| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/django-reversion-compare/20120508_django-reversion-compare_v0_1_0-03.png\n\n----\n\nExample screenshot from **v0.3.0**: a many-to-many field compare (friends, hobbies):\n\n|django-reversion-compare_v0_3_0-01.png|\n\n.. |django-reversion-compare_v0_3_0-01.png| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/django-reversion-compare/20120516_django-reversion-compare_v0_3_0-01.png\n\n* In the first line, the m2m object has been changed.\n\n* line 2: A m2m object was deleted\n\n* line 3: A m2m object was removed from this entry (but not deleted)\n\n* line 4: This m2m object has not changed\n\n----------------------------\ncreate developer environment\n----------------------------\n\ne.g.:\n\n::\n\n    # Clone project (Use your fork SSH url!):\n    ~$ git clone https://github.com/jedie/django-reversion-compare.git\n    ~$ cd django-reversion-compare\n    ~/django-reversion-compare$ make install\n    ~/django-reversion-compare$ make\n    help                 List all commands\n    install-poetry       install or update poetry\n    install              install reversion_compare via poetry\n    lint                 Run code formatters and linter\n    fix-code-style       Fix code formatting\n    tox-listenvs         List all tox test environments\n    tox                  Run pytest via tox with all environments\n    tox-py36             Run pytest via tox with *python v3.6*\n    tox-py37             Run pytest via tox with *python v3.7*\n    tox-py38             Run pytest via tox with *python v3.8*\n    pytest               Run pytest\n    update-rst-readme    update README.rst from README.reversion_compare\n    publish              Release new version to PyPi\n    run-test-server      Start Django dev server with the test project\n\nHelpful for writing and debugging unittests is to run a local test server with the same data.\ne.g.:\n\n::\n\n    ~/django-reversion-compare$ make run-test-server\n\n**migration** will be run.\n\nCall manage commands from test project, e.g.:\n\n::\n\n    ~/django-reversion-compare$ poetry shell\n    django-reversion-compare-foobar-py3.6) ~/django-reversion-compare$ ./reversion_compare_tests/manage.py --help\n    ...\n\n------------------------------\nBackwards-incompatible changes\n------------------------------\n\nv0.12.0\n=======\n\nGoogle "diff-match-patch" is now mandatory and not optional.\n\n---------------------\nVersion compatibility\n---------------------\n\n+-------------------+------------------+--------------------+------------------------------------------------+\n| Reversion-Compare | django-reversion | Django             | Python                                         |\n+===================+==================+====================+================================================+\n| >=v0.13.0         | v3.0             | v2.2, v3.0, v3.1   | v3.7, v3.8, v3.9                               |\n+-------------------+------------------+--------------------+------------------------------------------------+\n| >=v0.10.0         | v3.0             | v2.2, v3.0         | v3.6, v3.7, v3.8, pypy3                        |\n+-------------------+------------------+--------------------+------------------------------------------------+\n| >=v0.9.0          | v2.0             | v2.2, v3.0         | v3.6, v3.7, v3.8, pypy3                        |\n+-------------------+------------------+--------------------+------------------------------------------------+\n| >=v0.8.6          | v2.0             | v1.11, v2.0        | v3.5, v3.6, v3.7, pypy3                        |\n+-------------------+------------------+--------------------+------------------------------------------------+\n| >=v0.8.4          | v2.0             | v1.8, v1.11, v2.0  | v3.5, v3.6, pypy3                              |\n+-------------------+------------------+--------------------+------------------------------------------------+\n| >=v0.8.3          | v2.0             | v1.8, v1.11        | v3.5, v3.6, pypy3                              |\n+-------------------+------------------+--------------------+------------------------------------------------+\n| v0.8.x            | v2.0             | v1.8, v1.10, v1.11 | v2.7, v3.4, v3.5, v3.6 (only with Django 1.11) |\n+-------------------+------------------+--------------------+------------------------------------------------+\n| >=v0.7.2          | v2.0             | v1.8, v1.9, v1.10  | v2.7, v3.4, v3.5                               |\n+-------------------+------------------+--------------------+------------------------------------------------+\n| v0.7.x            | v2.0             | v1.8, v1.9         | v2.7, v3.4, v3.5                               |\n+-------------------+------------------+--------------------+------------------------------------------------+\n| v0.6.x            | v1.9, v1.10      | v1.8, v1.9         | v2.7, v3.4, v3.5                               |\n+-------------------+------------------+--------------------+------------------------------------------------+\n| >=v0.5.2          | v1.9             | v1.7, v1.8         | v2.7, v3.4                                     |\n+-------------------+------------------+--------------------+------------------------------------------------+\n| >=v0.4            | v1.8             | v1.7               | v2.7, v3.4                                     |\n+-------------------+------------------+--------------------+------------------------------------------------+\n| <v0.4             | v1.6             | v1.4               | v2.7                                           |\n+-------------------+------------------+--------------------+------------------------------------------------+\n\nThese are the unittests variants. See also: `/pyproject.toml <https://github.com/jedie/django-reversion-compare/blob/master/pyproject.toml>`_\nMaybe other versions are compatible, too.\n\n---------\nChangelog\n---------\n\n* *dev* `compare v0.13.1...master <https://github.com/jedie/django-reversion-compare/compare/v0.13.1...master>`_ \n\n    * TBC\n\n* v0.13.1 - 04.02.2021 `compare v0.13.0...v0.13.1 <https://github.com/jedie/django-reversion-compare/compare/v0.13.0...v0.13.1>`_ \n\n    * `Multiline diff formatting improvements <https://github.com/jedie/django-reversion-compare/pull/137>`_ contributed by dbader\n\n    * `Fix django.conf.urls.url() is deprecated <https://github.com/jedie/django-reversion-compare/pull/141>`_ contributed by GeyseR\n\n    * Add demo links to ``HistoryCompareDetailView`` in test project\n\n    * update github actions\n\n* v0.13.0 - 23.12.2020 `compare v0.12.2...v0.13.0 <https://github.com/jedie/django-reversion-compare/compare/v0.12.2...v0.13.0>`_ \n\n    * Support Django v3.1\n\n    * Stop running test with Python 3.6 and pypy3\n\n    * Activate django-debug-toolbar in test project\n\n    * code style (e.g.: f-strings) and remove some warnings in test project\n\n    * some project setup updates (e.g.: fix Python and Django version restrictions)\n\n* v0.12.2 - 24.03.2020 `compare v0.12.1...v0.12.2 <https://github.com/jedie/django-reversion-compare/compare/v0.12.1...v0.12.2>`_ \n\n    * `Added revert button on compare view <https://github.com/jedie/django-reversion-compare/pull/130>`_, contributed by jjarthur\n\n* v0.12.1 - 20.03.2020 `compare v0.12.0...v0.12.1 <https://github.com/jedie/django-reversion-compare/compare/v0.12.0...v0.12.1>`_ \n\n    * `Bugfix: Django 3.0 compatibility by change project dependencies <https://github.com/jedie/django-reversion-compare/pull/125>`_, contributed by maxocub\n\n    * Test project used a "auto login test user" middleware\n\n    * Test project rename django admin title and branding\n\n* v0.12.0 - 12.03.2020 `compare v0.11.0...v0.12.0 <https://github.com/jedie/django-reversion-compare/compare/v0.11.0...v0.12.0>`_ \n\n    * `google-diff-match-patch <https://github.com/google/diff-match-patch>`_ is now mandatory!\n\n    * Diff html code are now unified to ``<pre class="highlight">...</pre>``\n\n    * Bugfix ``make run-test-server``\n\n    * Switch between Google "diff-match-patch" and ``difflib.ndiff()`` by size: ndiff makes more human readable diffs with small values.\n\n* v0.11.0 - 12.03.2020 `compare v0.10.0...v0.11.0 <https://github.com/jedie/django-reversion-compare/compare/v0.10.0...v0.11.0>`_ \n\n    * CHANGE output of diff generated with "diff-match-patch":\n\n        * cleanup html by implement a own html pretty function instead of ``diff_match_patch.diff_prettyHtml`` usage\n\n        * The html is now simmilar to the difflib usage output and doesn\'t contain inline styles\n\n    * Add "diff-match-patch" as optional dependencies in poetry config\n\n    * Bugfix Django requirements\n\n    * code cleanup and update tests\n\n* v0.10.0 - 19.02.2020 `compare v0.9.1...v0.10.0 <https://github.com/jedie/django-reversion-compare/compare/v0.9.1...v0.10.0>`_ \n\n    * less restricted dependency specification see: `issues #120 <https://github.com/jedie/django-reversion-compare/issues/120>`_\n\n    * run tests with latest django-reversion version (currently v3.x)\n\n* v0.9.1 - 16.02.2020 `compare v0.9.0...v0.9.1 <https://github.com/jedie/django-reversion-compare/compare/v0.9.0...v0.9.1>`_ \n\n    * Modernize project setup and use poetry\n\n    * Apply pyupgrade and fix/update some f-strings\n\n    * Update test project\n\n* v0.9.0 - 19.01.2020 `compare v0.8.7...v0.9.0 <https://github.com/jedie/django-reversion-compare/compare/v0.8.7...v0.9.0>`_ \n\n    * Test with Python 3.8 and Django 3.0, too.\n\n    * Run tests via github actions, too.\n\n    * Remove support for Python 3.5 and Django v1.11\n\n    * `actually check if model is registered #115 <https://github.com/jedie/django-reversion-compare/pull/115>`_ contributed by willtho89\n\n    * `Remove python2 compatibility decorators #113 <https://github.com/jedie/django-reversion-compare/pull/113>`_ contributed by jeremy-engel\n\n    * `Show username and full name from custom user model #112 <https://github.com/jedie/django-reversion-compare/pull/112>`_ contributed by berekuk\n\n    * `Fix django-suit NoneType is not iterable #111 <https://github.com/jedie/django-reversion-compare/pull/111>`_ contributed by creativequality\n\n    * convert old format to f-strings via flynt\n\n    * Code style:\n\n        * sort imports with isort\n\n        * apply autopep8\n\n        * lint code in CI with flake8, isort and flynt\n\n* v0.8.7 - 06.01.2020 `compare v0.8.6...v0.8.7 <https://github.com/jedie/django-reversion-compare/compare/v0.8.6...v0.8.7>`_ \n\n    * Add new optional settings ``REVERSION_COMPARE_IGNORE_NOT_REGISTERED``, see: `issues #103 <https://github.com/jedie/django-reversion-compare/issues/103>`_\n\n    * reformat code with \'black\'\n\n    * some code cleanup\n\n* v0.8.6 - 04.01.2019 `compare v0.8.5...v0.8.6 <https://github.com/jedie/django-reversion-compare/compare/v0.8.5...v0.8.6>`_ \n\n    * Bugfix: `Use ".pk" instead of ".id" when referring to related object. <https://github.com/jedie/django-reversion-compare/pull/110>`_ contributed by `Peter Lisák <https://github.com/peterlisak>`_\n\n    * Run tests: Skip Django v1.8 and add Python v3.7\n\n* v0.8.5 - 13.09.2018 `compare v0.8.4...v0.8.5 <https://github.com/jedie/django-reversion-compare/compare/v0.8.4...v0.8.5>`_ \n\n    * `speed up delete checking <https://github.com/jedie/django-reversion-compare/pull/106>`_ contributed by `LegoStormtroopr <https://github.com/LegoStormtroopr>`_\n\n* v0.8.4 - 15.03.2018 `compare v0.8.3...v0.8.4 <https://github.com/jedie/django-reversion-compare/compare/v0.8.3...v0.8.4>`_ \n\n    * `Add Django 2.0 compatibility <https://github.com/jedie/django-reversion-compare/pull/102>`_ contributed by `samifahed <https://github.com/samifahed>`_\n\n* v0.8.3 - 21.12.2017 `compare v0.8.2...v0.8.3 <https://github.com/jedie/django-reversion-compare/compare/v0.8.2...v0.8.3>`_ \n\n    * refactor travis/tox/pytest/coverage stuff\n\n    * Tests can be run via ``python3 setup.py tox`` and/or ``python3 setup.py test``\n\n    * Test also with pypy3 on Travis CI.\n\n* `v0.8.2 - 06.12.2017 <https://github.com/jedie/django-reversion-compare/compare/v0.8.1...v0.8.2>`_:\n\n    * `Change ForeignKey relation compare <https://github.com/jedie/django-reversion-compare/pull/100>`_ contributed by `alaruss <https://github.com/alaruss>`_\n\n    * `Work around a type error triggered by taggit <https://github.com/jedie/django-reversion-compare/pull/86>`_ contributed by `Athemis <https://github.com/Athemis>`_\n\n    * minor code changes\n\n* `v0.8.1 - 02.10.2017 <https://github.com/jedie/django-reversion-compare/compare/v0.8.0...v0.8.1>`_:\n\n    * `Add added polish translation <https://github.com/jedie/django-reversion-compare/pull/99>`_ contributed by `w4rri0r3k <https://github.com/w4rri0r3k>`_\n\n    * Bugfix "Django>=1.11" in setup.py\n\n* `v0.8.0 - 17.08.2017 <https://github.com/jedie/django-reversion-compare/compare/v0.7.5...v0.8.0>`_:\n\n    * Run tests with Django v1.11 and drop tests with Django v1.9\n\n* `v0.7.5 - 24.04.2017 <https://github.com/jedie/django-reversion-compare/compare/v0.7.4...v0.7.5>`_:\n\n    * `Using the \'render\' function to ensure the execution of context processors properly <https://github.com/jedie/django-reversion-compare/pull/90>`_ contributed by `Rodrigo Pinheiro Marques de Araújo <https://github.com/fenrrir>`_\n\n* `v0.7.4 - 10.04.2017 <https://github.com/jedie/django-reversion-compare/compare/v0.7.3...v0.7.4>`_:\n\n    * Bugfix for Python 2: `compare unicode instead of bytes <https://github.com/jedie/django-reversion-compare/issues/89>`_ contributed by `Maksim Iakovlev <https://github.com/lampslave>`_\n\n    * `remove \'Django20Warning\' <https://github.com/jedie/django-reversion-compare/pull/88>`_ contributed by `Hugo Tácito <https://github.com/hugotacito>`_\n\n    * `Add \'Finnish\' localisations <https://github.com/jedie/django-reversion-compare/pull/87>`_ contributed by `Olli-Pekka Puolitaival <https://github.com/OPpuolitaival>`_\n\n* `v0.7.3 - 08.02.2017 <https://github.com/jedie/django-reversion-compare/compare/v0.7.2...v0.7.3>`_:\n\n    * `Fix case when model has template field which is ForeignKey <https://github.com/jedie/django-reversion-compare/pull/85>`_ contributed by `Lagovas <https://github.com/Lagovas>`_\n\n* `v0.7.2 - 20.10.2016 <https://github.com/jedie/django-reversion-compare/compare/v0.7.1...v0.7.2>`_:\n\n    * Add Django v1.10 support\n\n* `v0.7.1 - 29.08.2016 <https://github.com/jedie/django-reversion-compare/compare/v0.7.0...v0.7.1>`_:\n\n    * `Fix #79: missing import if **ADD_REVERSION_ADMIN != True** <https://github.com/jedie/django-reversion-compare/issues/79>`_\n\n* `v0.7.0 - 25.08.2016 <https://github.com/jedie/django-reversion-compare/compare/v0.6.3...v0.7.0>`_:\n\n    * `support only django-reversion >= 2.0 <https://github.com/jedie/django-reversion-compare/pull/76>`_ based on a contribution by `mshannon1123 <https://github.com/jedie/django-reversion-compare/pull/73>`_\n\n    * remove internal **reversion_api**\n\n    * Use tox\n\n* `v0.6.3 - 14.06.2016 <https://github.com/jedie/django-reversion-compare/compare/v0.6.2...v0.6.3>`_:\n\n    * `Remove unused and deprecated patters <https://github.com/jedie/django-reversion-compare/pull/69>`_ contributed by `codingjoe <https://github.com/codingjoe>`_\n\n    * `Fix django 1.10 warning #66 <https://github.com/jedie/django-reversion-compare/pull/66>`_ contributed by `pypetey <https://github.com/pypetey>`_\n\n* `v0.6.2 - 27.04.2016 <https://github.com/jedie/django-reversion-compare/compare/v0.6.1...v0.6.2>`_:\n\n    * `Added choices field representation #63 <https://github.com/jedie/django-reversion-compare/pull/63>`_ contributed by `amureki <https://github.com/amureki>`_\n\n    * `Check if related model has an integer as pk for ManyToMany fields. #64 <https://github.com/jedie/django-reversion-compare/pull/64>`_ contributed by `logaritmisk <https://github.com/logaritmisk>`_\n\n* `v0.6.1 - 16.02.2016 <https://github.com/jedie/django-reversion-compare/compare/v0.6.0...v0.6.1>`_:\n\n    * `pull #61 <https://github.com/jedie/django-reversion-compare/pull/61>`_: Fix error when ManyToMany relations didn\'t exist contributed by `Diederik van der Boor <https://github.com/vdboor>`_\n\n* `v0.6.0 - 03.02.2016 <https://github.com/jedie/django-reversion-compare/compare/v0.5.6...v0.6.0>`_:\n\n    * Added Dutch translation contributed by `Sae X <https://github.com/SaeX>`_\n\n    * Add support for Django 1.9\n\n    * Nicer boolean compare: `#57 <https://github.com/jedie/django-reversion-compare/issues/57>`_\n\n    * Fix `#58 compare followed reverse foreign relation fields that are on a non-abstract parent class <https://github.com/jedie/django-reversion-compare/issues/58>`_ contributed by LegoStormtroopr\n\n* `v0.5.6 - 23.09.2015 <https://github.com/jedie/django-reversion-compare/compare/v0.5.5...v0.5.6>`_:\n\n    * NEW: Class-Based-View to create non-admin views and greek translation contributed by `Serafeim Papastefanos <https://github.com/spapas>`_.\n\n* `v0.5.5 - 24.07.2015 <https://github.com/jedie/django-reversion-compare/compare/v0.5.4...v0.5.5>`_:\n\n    * UnboundLocalError (\'version\') when creating deleted list in get_many_to_something() `#41 <https://github.com/jedie/django-reversion-compare/pull/41>`_\n\n* `v0.5.4 - 22.07.2015 <https://github.com/jedie/django-reversion-compare/compare/v0.5.3...v0.5.4>`_:\n\n    * One to one field custom related name fix `#42 <https://github.com/jedie/django-reversion-compare/pull/42>`_ (contributed by frwickst and aemdy)\n\n* `v0.5.3 - 13.07.2015 <https://github.com/jedie/django-reversion-compare/compare/v0.5.2...v0.5.3>`_:\n\n    * Update admin.py to avoid RemovedInDjango19Warning (contributed by luzfcb)\n\n* `v0.5.2 - 14.04.2015 <https://github.com/jedie/django-reversion-compare/compare/v0.5.1...v0.5.2>`_:\n\n    * contributed by Samuel Spencer:\n\n        * Added Django 1.8 support: `pull #35 <https://github.com/jedie/django-reversion-compare/pull/35>`_\n\n        * list of changes for reverse fields incorrectly includes a "deletion" for the item that was added in: `issues #34 <https://github.com/jedie/django-reversion-compare/issues/34>`_\n\n* `v0.5.1 - 28.02.2015 <https://github.com/jedie/django-reversion-compare/compare/v0.5.0...v0.5.1>`_:\n\n    * activate previous/next links and add unitests for them\n\n* `v0.5.0 - 27.02.2015 <https://github.com/jedie/django-reversion-compare/compare/v0.4.0...v0.5.0>`_:\n\n    * refactory unittests, test with Django v1.7 and Python 2.7 & 3.4\n\n* `v0.4.0 - 02.02.2015 <https://github.com/jedie/django-reversion-compare/compare/v0.3.5...v0.4.0>`_:\n\n    * Updates for django 1.7 support\n\n    * Add ``settings.ADD_REVERSION_ADMIN``\n\n* v0.3.5 - 03.01.2013:\n\n    * Remove date from version string. `issues 9 <https://github.com/jedie/django-reversion-compare/issues/9>`_\n\n* v0.3.4 - 20.06.2012:\n\n    * Use VersionAdmin.revision_manager rather than default_revision_manager, contributed by Mark Lavin - see: `pull request 7 <https://github.com/jedie/django-reversion-compare/pull/7>`_\n\n    * Use logging for all debug prints, contributed by Bojan Mihelac - see: `pull request 8 <https://github.com/jedie/django-reversion-compare/pull/8>`_\n\n* v0.3.3 - 11.06.2012:\n\n    * Bugfix "ValueError: zero length field name in format" with Python 2.6 `issues 5 <https://github.com/jedie/django-reversion-compare/issues/5>`_\n\n* v0.3.2 - 04.06.2012:\n\n    * Bugfix for Python 2.6 in unified_diff(), see: `AttributeError: \'module\' object has no attribute \'_format_range_unified\' <https://github.com/jedie/django-reversion-compare/issues/5>`_\n\n* v0.3.1 - 01.06.2012:\n\n    * Bugfix: force unicode in html diff\n\n    * Bugfix in unittests\n\n* v0.3.0 - 16.05.2012:\n\n    * Enhanced handling of m2m changes with follow and non-follow relations.\n\n* v0.2.2 - 15.05.2012:\n\n    * Compare many-to-many in the right way.\n\n* v0.2.1 - 10.05.2012:\n\n    * Bugfix for models which has no m2m field: `https://github.com/jedie/django-reversion-compare/commit/c8e042945a6e78e5540b6ae27666f9b0cfc94880 <https://github.com/jedie/django-reversion-compare/commit/c8e042945a6e78e5540b6ae27666f9b0cfc94880>`_\n\n* v0.2.0 - 09.05.2012:\n\n    * many-to-many compare works, too.\n\n* v0.1.0 - 08.05.2012:\n\n    * First release\n\n* v0.0.1 - 08.05.2012:\n\n    * collect all compare stuff from old "diff" branch\n\n    * see also: `https://github.com/etianen/django-reversion/issues/147 <https://github.com/etianen/django-reversion/issues/147>`_\n\n-----\nLinks\n-----\n\n+-----------------+-------------------------------------------------------+\n| Github          | `https://github.com/jedie/django-reversion-compare`_  |\n+-----------------+-------------------------------------------------------+\n| Python Packages | `https://pypi.org/project/django-reversion-compare/`_ |\n+-----------------+-------------------------------------------------------+\n\n.. _https://github.com/jedie/django-reversion-compare: https://github.com/jedie/django-reversion-compare\n.. _https://pypi.org/project/django-reversion-compare/: https://pypi.org/project/django-reversion-compare/\n\n--------\nDonation\n--------\n\n* `paypal.me/JensDiemer <https://www.paypal.me/JensDiemer>`_\n\n* `Flattr This! <https://flattr.com/submit/auto?uid=jedie&url=https%3A%2F%2Fgithub.com%2Fjedie%2Fdjango-reversion-compare%2F>`_\n\n* Send `Bitcoins <https://www.bitcoin.org/>`_ to `1823RZ5Md1Q2X5aSXRC5LRPcYdveCiVX6F <https://blockexplorer.com/address/1823RZ5Md1Q2X5aSXRC5LRPcYdveCiVX6F>`_\n\n------------\n\n``Note: this file is generated from README.creole 2021-02-04 04:45:14 with "python-creole"``',
    'author': 'Jens Diemer',
    'author_email': 'django-reversion-compare@jensdiemer.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jedie/django-reversion-compare/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0.0',
}


setup(**setup_kwargs)
