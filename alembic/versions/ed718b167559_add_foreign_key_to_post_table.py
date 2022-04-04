"""add foreign key to post table

Revision ID: ed718b167559
Revises: 09a6e386571f
Create Date: 2022-04-03 15:28:26.712421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed718b167559'
down_revision = '09a6e386571f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fk', source_table = "posts", referent_table="users", local_cols= ['owner_id'], remote_cols= ['id'], ondelete= "CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
