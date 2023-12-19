"""categoria

Revision ID: e2a1b11f0399
Revises: c643affe7eba
Create Date: 2023-12-19 13:41:45.542758

"""
from typing import Sequence, Union

from datetime import datetime 
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2a1b11f0399'
down_revision: Union[str, None] = 'c643affe7eba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'categorias',
        sa.Column('id',sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('nombre', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)
    )
   


def downgrade() -> None:
    op.drop_table('categorias')