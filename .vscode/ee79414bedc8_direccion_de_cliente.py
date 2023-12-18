"""direccion_de_cliente

Revision ID: ee79414bedc8
Revises: 441533110b83
Create Date: 2023-12-14 14:05:54.255187

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee79414bedc8'
down_revision: Union[str, None] = '441533110b83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'direccion_de_cliente',
        sa.Column('calle', sa.String(45), nullable=False),
        sa.Column('sector', sa.String(45), nullable=False),
        sa.Column('comuna', sa.String(45), nullable=False),
        sa.Column('ciudad', sa.String(45), nullable=False),
        sa.Column('cliente_id', sa.Integer, sa.ForeignKey('clientes.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False),
    )

   


def downgrade() -> None:
    op.drop_table("direccion_de_cliente")