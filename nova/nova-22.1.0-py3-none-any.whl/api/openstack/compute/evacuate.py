#   Copyright 2013 OpenStack Foundation
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.


from oslo_log import log as logging
from oslo_utils import strutils
from webob import exc

from nova.api.openstack import api_version_request
from nova.api.openstack import common
from nova.api.openstack.compute.schemas import evacuate
from nova.api.openstack import wsgi
from nova.api import validation
from nova.compute import api as compute
import nova.conf
from nova import exception
from nova.i18n import _
from nova.network import neutron
from nova.policies import evacuate as evac_policies
from nova import utils

CONF = nova.conf.CONF

LOG = logging.getLogger(__name__)


class EvacuateController(wsgi.Controller):
    def __init__(self):
        super(EvacuateController, self).__init__()
        self.compute_api = compute.API()
        self.host_api = compute.HostAPI()
        self.network_api = neutron.API()

    def _get_on_shared_storage(self, req, evacuate_body):
        if api_version_request.is_supported(req, min_version='2.14'):
            return None
        else:
            return strutils.bool_from_string(evacuate_body["onSharedStorage"])

    def _get_password(self, req, evacuate_body, on_shared_storage):
        password = None
        if 'adminPass' in evacuate_body:
            # check that if requested to evacuate server on shared storage
            # password not specified
            if on_shared_storage:
                msg = _("admin password can't be changed on existing disk")
                raise exc.HTTPBadRequest(explanation=msg)

            password = evacuate_body['adminPass']
        elif not on_shared_storage:
            password = utils.generate_password()

        return password

    def _get_password_v214(self, req, evacuate_body):
        if 'adminPass' in evacuate_body:
            password = evacuate_body['adminPass']
        else:
            password = utils.generate_password()

        return password

    # TODO(eliqiao): Should be responding here with 202 Accept
    # because evacuate is an async call, but keep to 200 for
    # backwards compatibility reasons.
    @wsgi.expected_errors((400, 403, 404, 409))
    @wsgi.action('evacuate')
    @validation.schema(evacuate.evacuate, "2.0", "2.13")
    @validation.schema(evacuate.evacuate_v214, "2.14", "2.28")
    @validation.schema(evacuate.evacuate_v2_29, "2.29", "2.67")
    @validation.schema(evacuate.evacuate_v2_68, "2.68")
    def _evacuate(self, req, id, body):
        """Permit admins to evacuate a server from a failed host
        to a new one.
        """
        context = req.environ["nova.context"]
        instance = common.get_instance(self.compute_api, context, id)
        context.can(evac_policies.BASE_POLICY_NAME,
                    target={'user_id': instance.user_id,
                            'project_id': instance.project_id})

        evacuate_body = body["evacuate"]
        host = evacuate_body.get("host")
        force = None

        on_shared_storage = self._get_on_shared_storage(req, evacuate_body)

        if api_version_request.is_supported(req, min_version='2.29'):
            force = body["evacuate"].get("force", False)
            force = strutils.bool_from_string(force, strict=True)
            if force is True and not host:
                message = _("Can't force to a non-provided destination")
                raise exc.HTTPBadRequest(explanation=message)
        if api_version_request.is_supported(req, min_version='2.14'):
            password = self._get_password_v214(req, evacuate_body)
        else:
            password = self._get_password(req, evacuate_body,
                                          on_shared_storage)

        if host is not None:
            try:
                self.host_api.service_get_by_compute_host(context, host)
            except (exception.ComputeHostNotFound,
                    exception.HostMappingNotFound):
                msg = _("Compute host %s not found.") % host
                raise exc.HTTPNotFound(explanation=msg)

        if instance.host == host:
            msg = _("The target host can't be the same one.")
            raise exc.HTTPBadRequest(explanation=msg)

        # We could potentially move this check to conductor and avoid the
        # extra API call to neutron when we support move operations with ports
        # having resource requests.
        if (common.instance_has_port_with_resource_request(
                instance.uuid, self.network_api) and not
                common.supports_port_resource_request_during_move()):
            LOG.warning("The evacuate action on a server with ports "
                        "having resource requests, like a port with a QoS "
                        "minimum bandwidth policy, is not supported until "
                        "every nova-compute is upgraded to Ussuri")
            msg = _("The evacuate action on a server with ports having "
                    "resource requests, like a port with a QoS minimum "
                    "bandwidth policy, is not supported by this cluster right "
                    "now")
            raise exc.HTTPBadRequest(explanation=msg)

        try:
            self.compute_api.evacuate(context, instance, host,
                                      on_shared_storage, password, force)
        except exception.InstanceInvalidState as state_error:
            common.raise_http_conflict_for_instance_invalid_state(state_error,
                    'evacuate', id)
        except exception.ComputeServiceInUse as e:
            raise exc.HTTPBadRequest(explanation=e.format_message())
        except exception.ForbiddenWithAccelerators as e:
            raise exc.HTTPForbidden(explanation=e.format_message())
        except exception.OperationNotSupportedForVTPM as e:
            raise exc.HTTPConflict(explanation=e.format_message())

        if (not api_version_request.is_supported(req, min_version='2.14') and
                CONF.api.enable_instance_password):
            return {'adminPass': password}
        else:
            return None
