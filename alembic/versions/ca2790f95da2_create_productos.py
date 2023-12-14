"""create productos

Revision ID: ca2790f95da2
Revises: 80686ebde2ac
Create Date: 2023-12-13 21:17:50.737683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = 'ca2790f95da2'
down_revision: Union[str, None] = '80686ebde2ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'productos',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('nombre', sa.String(45), nullable=False),
        sa.Column("precio_compra", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("precio_venta", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("descripcion", sa.String(45),),
        sa.Column('categories_id', sa.Integer, sa.ForeignKey('categories.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
    )
    

def downgrade() -> None:
    op.drop_table("productos")