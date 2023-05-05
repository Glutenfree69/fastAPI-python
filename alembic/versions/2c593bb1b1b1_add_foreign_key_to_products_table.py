"""add foreign key to products table

Revision ID: 2c593bb1b1b1
Revises: 1ac4775cacd6
Create Date: 2023-05-05 10:57:20.051982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c593bb1b1b1'
down_revision = '1ac4775cacd6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('products', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('products_users_fk', source_table="products", referent_table="users", local_cols=['user_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('products_users_fk', table_name="products")
    op.drop_column('products', 'user_id')
    pass
