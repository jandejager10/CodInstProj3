"""Add is_admin to User and user_id to Book

Revision ID: a76c28e8db14
Revises: b75fbaca0a9c
Create Date: 2024-07-05 15:47:42.187737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a76c28e8db14'
down_revision = 'b75fbaca0a9c'
branch_labels = None
depends_on = None


def upgrade():
    # Add the column as nullable first
    op.add_column('book', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('is_admin', sa.Boolean(), nullable=True, server_default=sa.false()))

    # Add a foreign key constraint
    op.create_foreign_key(None, 'book', 'user', ['user_id'], ['id'])

    # Populate the user_id column with a default value
    connection = op.get_bind()
    connection.execute(
        sa.text('UPDATE book SET user_id = (SELECT id FROM "user" LIMIT 1)')
    )

    # Make the column non-nullable
    op.alter_column('book', 'user_id', existing_type=sa.Integer(), nullable=False)

def downgrade():
    # Drop the foreign key constraint
    op.drop_constraint(None, 'book', type_='foreignkey')

    # Drop the columns
    op.drop_column('user', 'is_admin')
    op.drop_column('book', 'user_id')