"""proveedor

Revision ID: da755cc97b85
Revises: 6b86f452cd2d
Create Date: 2023-12-14 20:01:18.766667

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da755cc97b85'
down_revision: Union[str, None] = '6b86f452cd2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'proveedores',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('nombre_de_proveedor', sa.String(45), nullable=False),
        sa.Column('rif', sa.String(45), nullable=False),
        sa.Column('telefono', sa.String(45), nullable=False),
        sa.Column('correo_electronico', sa.String(45), nullable=False),
        sa.Column('direccion_proveedor_id', sa.Integer, sa.ForeignKey('direccion_proveedor.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
        )
   


def downgrade() -> None:
     op.drop_table("proveedores")