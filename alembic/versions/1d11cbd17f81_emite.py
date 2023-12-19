"""emite

Revision ID: 1d11cbd17f81
Revises: 8e0e11c4f427
Create Date: 2023-12-19 14:08:43.457633

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d11cbd17f81'
down_revision: Union[str, None] = '8e0e11c4f427'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'emites',
        sa.Column('cantidad', sa.Integer, nullable=False),
        sa.Column('cantidad_emitida', sa.Integer, nullable=False),
        sa.Column('producto_id', sa.Integer, sa.ForeignKey('productos.id'), nullable=False),
        sa.Column('venta_id', sa.Integer, sa.ForeignKey('ventas.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
    )
   


def downgrade() -> None:
    op.drop_table('emites')
    
