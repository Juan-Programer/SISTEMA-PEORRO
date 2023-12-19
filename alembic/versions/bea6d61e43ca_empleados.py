"""empleados

Revision ID: bea6d61e43ca
Revises:
Create Date: 2023-12-17 13:47:37.856233

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bea6d61e43ca'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'empleados',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('cedula', sa.String(45), nullable=False),
        sa.Column('nombre', sa.String(45), nullable=False),
        sa.Column('apellido', sa.String(45), nullable=False),
        sa.Column('usuario', sa.String(50), nullable=False),
        sa.Column('contrasena', sa.String(250), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
    )



def downgrade() -> None:
    op.drop_table("empleados"),
