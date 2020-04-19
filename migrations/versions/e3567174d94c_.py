"""empty message

Revision ID: e3567174d94c
Revises: 2029f169a2ea
Create Date: 2020-04-17 14:23:27.915992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3567174d94c'
down_revision = '2029f169a2ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recruits', sa.Column('personal_email_address', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'recruits', ['personal_email_address'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recruits', type_='unique')
    op.drop_column('recruits', 'personal_email_address')
    # ### end Alembic commands ###
