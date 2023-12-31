"""Adding column x.

Revision ID: 2bbee0d9c6f3
Revises: 6c746030e1dd
Create Date: 2023-07-15 13:58:00.667522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bbee0d9c6f3'
down_revision = '6c746030e1dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('recovery_question', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('country', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('territory_state', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('dob', sa.String(length=80), nullable=False))
        batch_op.create_unique_constraint(None, ['country'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('dob')
        batch_op.drop_column('territory_state')
        batch_op.drop_column('country')
        batch_op.drop_column('recovery_question')

    # ### end Alembic commands ###
