"""empty message

Revision ID: d4f30fbb038a
Revises: 
Create Date: 2019-08-07 16:09:45.608010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4f30fbb038a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('image_file', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('followers_following',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('followers', sa.String(length=20), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('song_file', sa.String(length=20), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments_on_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comments', sa.String(length=200), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('postID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['postID'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments_on_post')
    op.drop_table('post')
    op.drop_table('followers_following')
    op.drop_table('user')
    # ### end Alembic commands ###