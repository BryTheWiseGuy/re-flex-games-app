"""change release date to date

Revision ID: 6b3afd87d7de
Revises: f26811762eb4
Create Date: 2023-10-05 11:22:19.707570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b3afd87d7de'
down_revision = 'f26811762eb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.alter_column('release_date',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.alter_column('release_date',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=False)

    # ### end Alembic commands ###
