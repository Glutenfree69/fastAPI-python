"""create products table

Revision ID: e0c50a11294c
Revises: 
Create Date: 2023-05-05 09:38:59.008405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0c50a11294c'
down_revision = None
branch_labels = None
depends_on = None


#upgrade permet de créer la table products et downgrade la supprimer si on en veut plus. Il faut coder la fonction soit même

def upgrade() -> None:
    op.create_table('products', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('description', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('products')
    pass
