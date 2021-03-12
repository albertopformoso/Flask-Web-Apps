"""initial migration

Revision ID: 5916daff2d42
Revises: 
Create Date: 2021-03-11 19:42:26.018139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5916daff2d42'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppy',
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppy')
    # ### end Alembic commands ###
