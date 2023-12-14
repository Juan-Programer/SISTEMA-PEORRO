"""create cliente

Revision ID: 09a9c4033b1f
Revises: ca2790f95da2
Create Date: 2023-12-14 13:21:21.929647

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision: str = '09a9c4033b1f'
down_revision: Union[str, None] = 'ca2790f95da2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'clientes',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('cedula', sa.Integer, nullable=False),
        sa.Column('nombre', sa.String(45), nullable=False),
        sa.Column('apellido', sa.String(45), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False),
    )
 


def downgrade() -> None:
    op.drop_table("clientes")