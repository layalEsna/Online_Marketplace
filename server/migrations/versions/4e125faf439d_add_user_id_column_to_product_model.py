"""Add user_id column to Product model

Revision ID: 4e125faf439d
Revises: 45d7b463719d
Create Date: 2025-01-27 22:54:10.601968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e125faf439d'
down_revision = '45d7b463719d'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False, server_default='1'))
        batch_op.create_foreign_key(batch_op.f('fk_products_user_id_users'), 'users', ['user_id'], ['id'])

    # Set default user_id for existing products
    op.execute('UPDATE products SET user_id = 1 WHERE user_id IS NULL')

def downgrade():
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_products_user_id_users'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
