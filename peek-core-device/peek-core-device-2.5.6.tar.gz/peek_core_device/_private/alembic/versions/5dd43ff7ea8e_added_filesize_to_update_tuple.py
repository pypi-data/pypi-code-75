"""added fileSize to update tuple

Peek Plugin Database Migration Script

Revision ID: 5dd43ff7ea8e
Revises: d94277dd8aca
Create Date: 2017-06-29 10:08:20.714750

"""

# revision identifiers, used by Alembic.
revision = '5dd43ff7ea8e'
down_revision = 'd94277dd8aca'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('DeviceUpdate', sa.Column('fileSize', sa.Integer(), nullable=False), schema='core_device')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('DeviceUpdate', 'fileSize', schema='core_device')
    # ### end Alembic commands ###