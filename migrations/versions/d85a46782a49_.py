"""empty message

Revision ID: d85a46782a49
Revises: 7dddc89bc464
Create Date: 2023-03-13 10:24:53.883663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd85a46782a49'
down_revision = '7dddc89bc464'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('default', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('permissions', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_roles_default'), ['default'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_roles_default'))
        batch_op.drop_column('permissions')
        batch_op.drop_column('default')

    # ### end Alembic commands ###
