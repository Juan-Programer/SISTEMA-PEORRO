"""telefono_cliente

Revision ID: 892f0356134c
Revises: f643e3b05f6f
Create Date: 2023-12-19 12:44:13.458662

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '892f0356134c'
down_revision: Union[str, None] = 'f643e3b05f6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'telefono_clientes',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('numero', sa.String(45), nullable=False ),
        sa.Column('cliente_id', sa.Integer, sa.ForeignKey('clientes.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False),


    )
    


def downgrade() -> None:
    op.drop_table('telefono_clientes')