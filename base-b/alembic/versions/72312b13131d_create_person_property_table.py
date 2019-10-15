"""create person_property table

Revision ID: 72312b13131d
Revises: e84eee4191df
Create Date: 2019-10-13 12:52:12.570674

"""
import sqlalchemy as sa
from alembic import op
# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey

revision = '72312b13131d'
down_revision = 'e84eee4191df'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'person_property',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('value', sa.Float(precision=2), nullable=False),
        sa.Column('description', sa.String(50), nullable=False),
        sa.Column('person_id', sa.Integer, ForeignKey('person.id'))
    )


def downgrade():
    op.drop_table('person_property')
