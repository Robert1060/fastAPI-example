"""create post table

Revision ID: 842d2ab8933c
Revises: 
Create Date: 2022-04-03 14:47:38.599835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '842d2ab8933c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
        sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
        sa.Column('title', sa.String(), nullable = False)
    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
