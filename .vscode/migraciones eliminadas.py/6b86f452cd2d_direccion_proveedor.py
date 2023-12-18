"""direccion_proveedor

Revision ID: 6b86f452cd2d
Revises: 458bf4ed06e7
Create Date: 2023-12-14 19:23:57.820899

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b86f452cd2d'
down_revision: Union[str, None] = '458bf4ed06e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'direccion_proveedores',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('calle', sa.String(45), nullable=False),
        sa.Column('comuna', sa.String(45), nullable=False),
        sa.Column('numero', sa.String(45), nullable=False),
        sa.Column('ciudad', sa.String(45), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)

        )
    


def downgrade() -> None:
    op.drop_table("direccion_proveedores")