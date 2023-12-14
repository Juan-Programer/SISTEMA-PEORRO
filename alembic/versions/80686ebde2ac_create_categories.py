"""create categories

Revision ID: 80686ebde2ac
Revises: 
Create Date: 2023-12-13 21:03:20.619927

"""
from typing import Sequence, Union
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80686ebde2ac'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'categorias',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('nombre', sa.String(45), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
    )

def downgrade() -> None:
    op.drop_table("categorias")
