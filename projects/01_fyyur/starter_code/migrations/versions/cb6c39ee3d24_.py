"""empty message

Revision ID: cb6c39ee3d24
Revises: 85bd25d0ed0e
Create Date: 2022-08-12 10:51:35.736099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb6c39ee3d24'
down_revision = '85bd25d0ed0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website_link', sa.String(length=500), nullable=True))
    op.add_column('Artist', sa.Column('venue', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description_artist', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'seeking_description_artist')
    op.drop_column('Artist', 'venue')
    op.drop_column('Artist', 'website_link')
    # ### end Alembic commands ###
