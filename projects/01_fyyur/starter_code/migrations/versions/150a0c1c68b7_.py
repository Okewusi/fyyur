"""empty message

Revision ID: 150a0c1c68b7
Revises: f8d6608b4d36
Create Date: 2022-08-13 09:52:07.795298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '150a0c1c68b7'
down_revision = 'f8d6608b4d36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('seeking_description', sa.String(), nullable=True))
    op.drop_column('artist', 'seeking_description_artist')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('seeking_description_artist', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('artist', 'seeking_description')
    # ### end Alembic commands ###
