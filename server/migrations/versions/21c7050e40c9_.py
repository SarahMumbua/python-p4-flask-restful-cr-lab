"""empty message

Revision ID: 21c7050e40c9
Revises: 30e77223e20d
Create Date: 2023-07-02 00:27:51.074553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21c7050e40c9'
down_revision = '30e77223e20d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###