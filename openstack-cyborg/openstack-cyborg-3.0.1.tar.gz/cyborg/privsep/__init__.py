# Copyright 2019 ZTE Corporation
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Setup privsep decorator."""

from oslo_privsep import capabilities
from oslo_privsep import priv_context

sys_admin_pctxt = priv_context.PrivContext(
    'cyborg',
    cfg_section='cyborg_sys_admin',
    pypath=__name__ + '.sys_admin_pctxt',
    # TODO(yumeng):
    # CAP_SYS_ADMIN has a lot of scary powers, so
    # consider breaking this out into a separate minimal context.
    capabilities=[capabilities.CAP_CHOWN,
                  capabilities.CAP_DAC_OVERRIDE,
                  capabilities.CAP_DAC_READ_SEARCH,
                  capabilities.CAP_FOWNER,
                  capabilities.CAP_SYS_ADMIN],
)
