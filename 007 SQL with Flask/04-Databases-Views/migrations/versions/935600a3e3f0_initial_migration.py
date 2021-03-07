"""initial migration

Revision ID: 935600a3e3f0
Revises: 
Create Date: 2021-03-07 10:08:39.669964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '935600a3e3f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppies')
    # ### end Alembic commands ###
