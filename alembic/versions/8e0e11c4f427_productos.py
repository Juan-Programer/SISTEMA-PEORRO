"""productos

Revision ID: 8e0e11c4f427
Revises: e2a1b11f0399
Create Date: 2023-12-19 13:47:57.999699

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e0e11c4f427'
down_revision: Union[str, None] = 'e2a1b11f0399'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'productos',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('nombre', sa.String, nullable=False),
        sa.Column('precio_compra', sa.Numeric(10,2), nullable=False),
        sa.Column('precio_venta', sa.Numeric(10,2), nullable=False),
        sa.Column('descripcion', sa.String, nullable=False),
        sa.Column('producto_inventario', sa.Integer, nullable=False),
        sa.Column('categoria_id', sa.Integer, sa.ForeignKey('categorias.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
    )
    


def downgrade() -> None:
    op.drop_table('productos')