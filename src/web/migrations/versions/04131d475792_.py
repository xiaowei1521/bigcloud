"""empty message

Revision ID: 04131d475792
Revises: 2306e6ea10d6
Create Date: 2017-01-12 17:25:49.932908

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '04131d475792'
down_revision = '2306e6ea10d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('functions', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('functions', '主键')
    op.add_column('littleclouds', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('littleclouds', '主键')
    op.add_column('packages', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('packages', '主键')
    op.add_column('users', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('users', '主键')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('主键', mysql.INTEGER(display_width=11), nullable=False))
    op.drop_column('users', 'id')
    op.add_column('packages', sa.Column('主键', mysql.INTEGER(display_width=11), nullable=False))
    op.drop_column('packages', 'id')
    op.add_column('littleclouds', sa.Column('主键', mysql.INTEGER(display_width=11), nullable=False))
    op.drop_column('littleclouds', 'id')
    op.add_column('functions', sa.Column('主键', mysql.INTEGER(display_width=11), nullable=False))
    op.drop_column('functions', 'id')
    # ### end Alembic commands ###
