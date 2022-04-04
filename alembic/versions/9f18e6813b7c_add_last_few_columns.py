"""add last few columns

Revision ID: 9f18e6813b7c
Revises: ed718b167559
Create Date: 2022-04-03 15:38:21.468474

"""


from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f18e6813b7c'
down_revision = 'ed718b167559'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable = False, server_default = 'TRUE'
    ),
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone = True), nullable = False, server_default = sa.text('NOW()')
    ))
    )

    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
