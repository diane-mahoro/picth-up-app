"""Initial Migration

Revision ID: 5345edf1b3ec
Revises: 426871cd2f7c
Create Date: 2019-09-19 12:23:09.246525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5345edf1b3ec'
down_revision = '426871cd2f7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_secure')
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
