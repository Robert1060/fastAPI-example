"""add content column

Revision ID: 12215e037704
Revises: 842d2ab8933c
Create Date: 2022-04-03 14:57:05.791688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12215e037704'
down_revision = '842d2ab8933c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
