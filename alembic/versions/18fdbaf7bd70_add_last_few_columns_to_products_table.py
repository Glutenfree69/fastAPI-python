"""add last few columns to products table

Revision ID: 18fdbaf7bd70
Revises: 2c593bb1b1b1
Create Date: 2023-05-05 11:09:20.823621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18fdbaf7bd70'
down_revision = '2c593bb1b1b1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('products', sa.Column('price', sa.Integer(), nullable=False),)
    op.add_column('products', sa.Column('image', sa.String(), nullable=False),)
    op.add_column('products', sa.Column('inventory', sa.Integer(), nullable=False),)
    op.add_column('products', sa.Column('public', sa.BOOLEAN(), nullable=False, server_default='FALSE'),)
    op.add_column('products', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),)
    pass


def downgrade() -> None:
    op.drop_column('products', 'price')
    op.drop_column('products', 'image')
    op.drop_column('products', 'inventory')
    op.drop_column('products', 'public')
    op.drop_column('products', 'created_at')
    pass
