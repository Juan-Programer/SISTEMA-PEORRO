"""provee

Revision ID: 7fec9580ae84
Revises: da755cc97b85
Create Date: 2023-12-14 20:10:54.790568

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7fec9580ae84'
down_revision: Union[str, None] = 'da755cc97b85'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None: 
    op.create_table(
        'provees',
        sa.Column('provedores_id', sa.Integer, sa.ForeignKey('proveedor.id'), nullable=False),
        sa.Column('producto_id', sa.Integer, sa.ForeignKey('productos.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
        )
    


def downgrade() -> None:
    op.drop_table("provees")