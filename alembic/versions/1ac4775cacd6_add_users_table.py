"""add users table

Revision ID: 1ac4775cacd6
Revises: b1aaf27f359c
Create Date: 2023-05-05 10:44:29.046293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ac4775cacd6'
down_revision = 'b1aaf27f359c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('role', sa.Integer(), nullable=False, server_default='0'),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('adresse', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email', 'username')
                    
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
