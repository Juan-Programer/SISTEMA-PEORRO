"""ventas

Revision ID: 12063c9aed08
Revises: ee79414bedc8
Create Date: 2023-12-14 14:50:26.701858

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12063c9aed08'
down_revision: Union[str, None] = 'ee79414bedc8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ventas',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('fecha', sa.DateTime, default = datetime.now(), nullable=False),
        sa.Column('empleado_id', sa.Integer, sa.ForeignKey('empleados.id'), nullable=False),
        sa.Column('cliente_id', sa.Integer, sa.ForeignKey('clientes.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False),
        
        )

   

def downgrade() -> None:
    op.drop_table("ventas")