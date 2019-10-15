"""create person_debts table

Revision ID: 4d6143fcfce6
Revises: 056a33657edf
Create Date: 2019-10-12 12:21:04.941159

"""
import sqlalchemy as sa
from alembic import op
# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey

revision = '66d6e2a0163e'
down_revision = '056a33657edf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'person_debts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('value', sa.Float(precision=2), nullable=False),
        sa.Column('description', sa.String(50), nullable=False),
        sa.Column('person_id', sa.Integer, ForeignKey('person.id'))
    )


def downgrade():
    op.drop_table('person_debts')
