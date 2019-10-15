"""create person table

Revision ID: e84eee4191df
Revises: 
Create Date: 2019-10-13 12:51:34.647519

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'e84eee4191df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'person',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('birth', sa.Date(), nullable=False),
        sa.Column('document', sa.String(100), nullable=False),
        sa.Column('wage', sa.Float(precision=2), nullable=False),
        sa.Column('address', sa.String(200), nullable=False)
    )


def downgrade():
    op.drop_table('person')
