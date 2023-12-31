"""create games table

Revision ID: f9296437f35d
Revises: a12d088d0bdf
Create Date: 2023-09-25 16:47:19.799665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9296437f35d'
down_revision = 'a12d088d0bdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('genre', sa.String(), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=False),
    sa.Column('publisher', sa.String(), nullable=False),
    sa.Column('game_image', sa.String(), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    # ### end Alembic commands ###
