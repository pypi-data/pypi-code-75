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

from sqlalchemy import MetaData
from sqlalchemy import Table

from nova.db.sqlalchemy import api_models


def upgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    request_specs = Table('request_specs', meta, autoload=True)
    if request_specs.c.spec.type != api_models.MediumText():
        request_specs.c.spec.alter(type=api_models.MediumText())
