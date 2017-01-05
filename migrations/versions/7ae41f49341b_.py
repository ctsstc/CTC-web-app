"""empty message

Revision ID: 7ae41f49341b
Revises: 8abcf8a389e3
Create Date: 2017-01-04 12:06:16.513063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ae41f49341b'
down_revision = '8abcf8a389e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('linkedin', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'linkedin')
    # ### end Alembic commands ###