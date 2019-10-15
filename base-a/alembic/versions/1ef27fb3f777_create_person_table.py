"""create person table

Revision ID: 1ef27fb3f777
Revises: 
Create Date: 2019-10-12 12:11:18.818103

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '056a33657edf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'person',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('document', sa.String(100), nullable=False),
        sa.Column('address', sa.String(200))
    )


def downgrade():
    op.drop_table('person')
