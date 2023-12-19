"""proveedor

Revision ID: 2cab6b31ddf9
Revises: 1d11cbd17f81
Create Date: 2023-12-19 14:24:42.472248

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2cab6b31ddf9'
down_revision: Union[str, None] = '1d11cbd17f81'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'proveedores',
        sa.Column('id',sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('nombre_de_proveedor', sa.String(45), nullable=False),
        sa.Column('rif', sa.String(60), nullable=False),
        sa.Column('telefono', sa.String(60), nullable=False),
        sa.Column('correo_electronico', sa.String(60), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
    )
   


def downgrade() -> None:
    op.drop_table('proveedores')
    
