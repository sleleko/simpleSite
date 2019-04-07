"""contents table

Revision ID: 273068979bd8
Revises: 011f2cf64831
Create Date: 2019-04-02 21:58:29.394532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '273068979bd8'
down_revision = '011f2cf64831'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=40), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('introtext', sa.String(length=120), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_content_timestamp'), 'content', ['timestamp'], unique=False)
    op.drop_index('ix_site_content_timestamp', table_name='site_content')
    op.drop_table('site_content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site_content',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('title', sa.VARCHAR(length=40), nullable=True),
    sa.Column('description', sa.VARCHAR(length=100), nullable=True),
    sa.Column('introtext', sa.VARCHAR(length=120), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('content', sa.VARCHAR(length=250), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_site_content_timestamp', 'site_content', ['timestamp'], unique=False)
    op.drop_index(op.f('ix_content_timestamp'), table_name='content')
    op.drop_table('content')
    # ### end Alembic commands ###