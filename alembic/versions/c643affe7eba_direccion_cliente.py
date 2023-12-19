"""direccion_cliente

Revision ID: c643affe7eba
Revises: 892f0356134c
Create Date: 2023-12-19 12:56:10.361123

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c643affe7eba'
down_revision: Union[str, None] = '892f0356134c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'direccion_clientes',
        sa.Column('id', sa.Integer,autoincrement=True, primary_key=True ),
        sa.Column('calle', sa.String, nullable=False),
        sa.Column('comuna', sa.String, nullable=False),
        sa.Column('numero', sa.String, nullable=False),
        sa.Column('ciudad', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False),

    )
    


def downgrade() -> None:
    op.drop_table('direccion_clientes')
