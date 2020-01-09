"""empty message

Revision ID: ba6f13ccbabb
Revises: d29cca963221
Create Date: 2020-01-08 21:23:06.288453

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba6f13ccbabb'
down_revision = 'd29cca963221'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('directory',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
    sa.Column('updated_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('gen_email', sa.Column('directory_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'gen_email', 'directory', ['directory_id'], ['id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'gen_email', type_='foreignkey')
    op.drop_column('gen_email', 'directory_id')
    op.drop_table('directory')
    # ### end Alembic commands ###