"""emite

Revision ID: 458bf4ed06e7
Revises: 51bdcb80182c
Create Date: 2023-12-14 18:05:35.639059

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '458bf4ed06e7'
down_revision: Union[str, None] = '51bdcb80182c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table(
           'emites',
           sa.Column("precio_venta", sa.Numeric(precision=10, scale=2), nullable=False),
           sa.Column('venta_id', sa.Integer, sa.ForeignKey('ventas.id'), nullable=False),
           sa.Column('producto_id', sa.Integer, sa.ForeignKey('productos.id'), nullable=False),
           sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
           sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
    )




    


def downgrade() -> None:
      op.drop_table("emites")