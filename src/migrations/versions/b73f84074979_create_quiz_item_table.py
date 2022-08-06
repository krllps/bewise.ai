"""Create quiz_item table

Revision ID: b73f84074979
Revises: 883ba1d7e89f
Create Date: 2022-08-06 12:42:04.898616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b73f84074979'
down_revision = '883ba1d7e89f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=512), nullable=False),
    sa.Column('answer', sa.String(length=512), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quiz_item_question'), 'quiz_item', ['question'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_quiz_item_question'), table_name='quiz_item')
    op.drop_table('quiz_item')
    # ### end Alembic commands ###