"""empty message

Revision ID: 097b49841805
Revises: 9644ab358b35
Create Date: 2019-05-29 16:31:38.969987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '097b49841805'
down_revision = '9644ab358b35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher', sa.Column('course_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'teacher', 'course', ['course_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teacher', type_='foreignkey')
    op.drop_column('teacher', 'course_id')
    # ### end Alembic commands ###