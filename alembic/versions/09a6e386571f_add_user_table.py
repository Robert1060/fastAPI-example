"""add user table

Revision ID: 09a6e386571f
Revises: 12215e037704
Create Date: 2022-04-03 15:16:26.562667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09a6e386571f'
down_revision = '12215e037704'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id',sa.Integer(), nullable = False),
        sa.Column('email', sa.String(), nullable = False),
        sa.Column('password', sa.Integer(), nullable = False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                    server_default = sa.text('now()'), nullable = False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
        )
    pass


def downgrade():
    op.drop_table('users')
    pass
