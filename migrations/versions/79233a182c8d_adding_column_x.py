"""Adding column x.

Revision ID: 79233a182c8d
Revises: b21160aa2d88
Create Date: 2023-07-15 13:35:15.770113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79233a182c8d'
down_revision = 'b21160aa2d88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=80), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###