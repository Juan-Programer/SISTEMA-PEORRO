"""provee

Revision ID: 75e4cc30e3d5
Revises: 9a2b6d36030c
Create Date: 2023-12-19 15:07:08.173993

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75e4cc30e3d5'
down_revision: Union[str, None] = '9a2b6d36030c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'provees',
        sa.Column('proveedor_id', sa.Integer, sa.ForeignKey('proveedores.id'), nullable=False),
        sa.Column('producto_id', sa.Integer, sa.ForeignKey('productos.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
    )
    

def downgrade() -> None:
    op.drop_table('provees')
    
