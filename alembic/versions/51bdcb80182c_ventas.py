"""ventas

Revision ID: 51bdcb80182c
Revises: 0818988399e7
Create Date: 2023-12-14 17:36:21.642916

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51bdcb80182c'
down_revision: Union[str, None] = '0818988399e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ventas',
       sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
       sa.Column('fecha', sa.DateTime, default=datetime.now(), nullable=False),
       sa.Column('empleado_id', sa.Integer, sa.ForeignKey('empleados.id'), nullable=False),
       sa.Column('cliente_id', sa.Integer, sa.ForeignKey('clientes.id'), nullable=False),
    )
    


def downgrade() -> None:
    op.drop_table("ventas")