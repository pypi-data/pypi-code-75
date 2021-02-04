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


from migrate import UniqueConstraint
from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table


def upgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    for prefix in ('', 'shadow_'):
        table = Table(prefix + 'block_device_mapping', meta, autoload=True)
        if not hasattr(table.c, 'uuid'):
            new_column = Column('uuid', String(36), nullable=True)
            table.create_column(new_column)

            if prefix == '':
                # Only add the constraint on the non-shadow table...
                con = UniqueConstraint('uuid', table=table,
                                       name="uniq_block_device_mapping0uuid")
                con.create(migrate_engine)
