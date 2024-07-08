"""empty message

Revision ID: fd1a2f92512d
Revises: 
Create Date: 2024-07-08 11:35:25.450430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd1a2f92512d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('accnum', sa.String(length=25), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Debit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=100), nullable=True),
    sa.Column('debit_amount', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['login.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Track_Deposite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=100), nullable=True),
    sa.Column('deposite_amount', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['login.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Track_Transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=100), nullable=True),
    sa.Column('transfer_amount', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['login.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('balance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('money', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['login.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('current',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['balance.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dollar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['balance.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('savings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['balance.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('utility',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['balance.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('utility')
    op.drop_table('savings')
    op.drop_table('dollar')
    op.drop_table('current')
    op.drop_table('balance')
    op.drop_table('Track_Transaction')
    op.drop_table('Track_Deposite')
    op.drop_table('Debit')
    op.drop_table('login')
    op.drop_table('admin')
    # ### end Alembic commands ###