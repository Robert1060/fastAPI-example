"""add phone number

Revision ID: e86774e37918
Revises: 193c26f5239d
Create Date: 2022-04-04 22:11:27.828538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e86774e37918'
down_revision = '193c26f5239d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
