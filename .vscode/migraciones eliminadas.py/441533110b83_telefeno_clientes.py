"""telefeno_clientes

Revision ID: 441533110b83
Revises: 09a9c4033b1f
Create Date: 2023-12-14 13:40:10.486325

"""
from typing import Sequence, Union

from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '441533110b83'
down_revision: Union[str, None] = '09a9c4033b1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table(
    'telefono_clientes',
    sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
    sa.Column('numero', sa.Integer, nullable=False),
    sa.Column('cliente_id', sa.Integer, sa.ForeignKey('clientes.id'), nullable=False),
    sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
    sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False),
     )




  


def downgrade() -> None:
    op.drop_table("telefono_clientes")
