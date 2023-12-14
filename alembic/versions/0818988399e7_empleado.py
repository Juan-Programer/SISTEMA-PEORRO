"""empleado

Revision ID: 0818988399e7
Revises: ee79414bedc8
Create Date: 2023-12-14 17:17:27.757995

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0818988399e7'
down_revision: Union[str, None] = 'ee79414bedc8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'empleados',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('cedula', sa.String(45), nullable=False),
        sa.Column('nombre', sa.String(45), nullable=False),
        sa.Column('apellido', sa.String(45), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
        )
    


def downgrade() -> None:
    op.drop_table("empleados")