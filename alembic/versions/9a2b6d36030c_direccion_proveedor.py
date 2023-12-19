"""direccion_proveedor

Revision ID: 9a2b6d36030c
Revises: 2cab6b31ddf9
Create Date: 2023-12-19 14:52:11.402131

"""
from typing import Sequence, Union

from datetime import datetime 
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a2b6d36030c'
down_revision: Union[str, None] = '2cab6b31ddf9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'direccion_provedores',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('calle', sa.String(45), nullable=False),
        sa.Column('comuna', sa.String(45), nullable=False),
        sa.Column('numero', sa.String(45), nullable=False),
        sa.Column('cuidad', sa.String(45), nullable=False),
        sa.Column('proveedor_id', sa.Integer, sa.ForeignKey('proveedores.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
    )



def downgrade() -> None:
    op.drop_table('direccion_proveedores')
   