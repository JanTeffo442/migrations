"""empty message

Revision ID: 6fb2196bcc00
Revises: e3567174d94c
Create Date: 2020-04-17 15:24:07.535364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fb2196bcc00'
down_revision = 'e3567174d94c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recruits', sa.Column('chort', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recruits', 'chort')
    # ### end Alembic commands ###
