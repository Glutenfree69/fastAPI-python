"""add name column to products

Revision ID: b1aaf27f359c
Revises: e0c50a11294c
Create Date: 2023-05-05 10:36:51.212976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1aaf27f359c'
down_revision = 'e0c50a11294c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('products', sa.Column('name', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('products', 'name')
    pass
