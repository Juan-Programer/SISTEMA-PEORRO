"""ventas

Revision ID: f643e3b05f6f
Revises: bb566da46c42
Create Date: 2023-12-19 11:39:46.212549

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f643e3b05f6f'
down_revision: Union[str, None] = 'bb566da46c42'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ventas',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('fecha', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('productos_vendidos', sa.String(45), nullable=False),
        sa.Column('precio_de_venta', sa.Numeric(45), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False),
        sa.Column('cliente_id', sa.Integer, sa.ForeignKey('clientes.id'),nullable=False),
        sa.Column('empleado_id', sa.Integer, sa.ForeignKey('empleados.id'),nullable=False)
    )
   


def downgrade() -> None:
    op.drop_table('ventas')
