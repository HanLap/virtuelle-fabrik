"""add produkt and material tables

Revision ID: 478f5dc0676e
Revises: 507ec2ed41be
Create Date: 2023-03-23 06:17:37.956921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '478f5dc0676e'
down_revision = '507ec2ed41be'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('material',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('kostenStueck', sa.Float(), nullable=True),
    sa.Column('bestand', sa.Float(), nullable=True),
    sa.Column('aufstockenMinute', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produkt',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('verkaufspreis', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('materialbedarf',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('menge', sa.Float(), nullable=True),
    sa.Column('material_id', sa.String(), nullable=False),
    sa.Column('produkt_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['material_id'], ['material.id'], ),
    sa.ForeignKeyConstraint(['produkt_id'], ['produkt.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produktionsschritt',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('schritt', sa.Integer(), nullable=True),
    sa.Column('produkt_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['produkt_id'], ['produkt.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produktionsschritt')
    op.drop_table('materialbedarf')
    op.drop_table('produkt')
    op.drop_table('material')
    # ### end Alembic commands ###
