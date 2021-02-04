"""added coordset mx c

Peek Plugin Database Migration Script

Revision ID: 4b943b584307
Revises: d103b9c1eba9
Create Date: 2017-10-01 11:16:34.264774

"""

# revision identifiers, used by Alembic.
revision = '4b943b584307'
down_revision = 'd103b9c1eba9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    op.add_column('ModelCoordSet', sa.Column('multiplierX', sa.Float(), server_default='1', nullable=True), schema='pl_diagram')
    op.add_column('ModelCoordSet', sa.Column('multiplierY', sa.Float(), server_default='1', nullable=True), schema='pl_diagram')
    op.add_column('ModelCoordSet', sa.Column('offsetX', sa.Float(), server_default='0', nullable=True), schema='pl_diagram')
    op.add_column('ModelCoordSet', sa.Column('offsetY', sa.Float(), server_default='0', nullable=True), schema='pl_diagram')

    op.execute('''UPDATE "pl_diagram"."ModelCoordSet"
                  SET "multiplierX" = 1,
                        "multiplierY" = 1,
                        "offsetX" = 0,
                        "offsetY" = 0
                       ''')

    op.alter_column('ModelCoordSet', 'multiplierX', type_=sa.Float, nullable=False, schema='pl_diagram')
    op.alter_column('ModelCoordSet', 'multiplierY', type_=sa.Float, nullable=False, schema='pl_diagram')
    op.alter_column('ModelCoordSet', 'offsetX', type_=sa.Float, nullable=False, schema='pl_diagram')
    op.alter_column('ModelCoordSet', 'offsetY', type_=sa.Float, nullable=False, schema='pl_diagram')
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ModelCoordSet', 'offsetY', schema='pl_diagram')
    op.drop_column('ModelCoordSet', 'offsetX', schema='pl_diagram')
    op.drop_column('ModelCoordSet', 'multiplierY', schema='pl_diagram')
    op.drop_column('ModelCoordSet', 'multiplierX', schema='pl_diagram')
    # ### end Alembic commands ###