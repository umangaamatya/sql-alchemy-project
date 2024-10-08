"""Update user table

Revision ID: 0d29713d4591
Revises: 6b275e0e11f4
Create Date: 2024-10-08 10:23:07.241597

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0d29713d4591'
down_revision = '6b275e0e11f4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('first_name', sa.String(length=50), nullable=False))
    op.add_column('user', sa.Column('last_name', sa.String(length=100), nullable=False))
    op.drop_column('user', 'name')


def downgrade():
    op.add_column('user', sa.Column('name', mysql.VARCHAR(length=50), nullable=False))
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
