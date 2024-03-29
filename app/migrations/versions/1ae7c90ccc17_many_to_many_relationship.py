"""many to many relationship

Revision ID: 1ae7c90ccc17
Revises: b2e2ec7b2a30
Create Date: 2024-01-09 00:05:08.464446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ae7c90ccc17'
down_revision = 'b2e2ec7b2a30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('first_name', sa.String(), nullable=True))
    op.add_column('customers', sa.Column('last_name', sa.String(), nullable=True))
    op.add_column('restaurants', sa.Column('name', sa.String(), nullable=True))
    op.add_column('restaurants', sa.Column('price', sa.Integer(), nullable=True))
    op.add_column('reviews', sa.Column('star_rating', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reviews', 'star_rating')
    op.drop_column('restaurants', 'price')
    op.drop_column('restaurants', 'name')
    op.drop_column('customers', 'last_name')
    op.drop_column('customers', 'first_name')
    # ### end Alembic commands ###
