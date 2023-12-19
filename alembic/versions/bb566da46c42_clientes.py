"""clientes

Revision ID: bb566da46c42
Revises: bea6d61e43ca
Create Date: 2023-12-19 11:32:39.856439

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb566da46c42'
down_revision: Union[str, None] = 'bea6d61e43ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'clientes',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('cedula', sa.String(45), nullable=False),
        sa.Column('nombre', sa.String(45), nullable=False),
        sa.Column('apellido', sa.String(45), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
    )

   

def downgrade() -> None:
    op.drop_table('clientes')