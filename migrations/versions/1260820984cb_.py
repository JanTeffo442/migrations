"""empty message

Revision ID: 1260820984cb
Revises: 6fb2196bcc00
Create Date: 2020-04-19 17:44:50.379977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1260820984cb'
down_revision = '6fb2196bcc00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recruits', 'chort')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recruits', sa.Column('chort', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
