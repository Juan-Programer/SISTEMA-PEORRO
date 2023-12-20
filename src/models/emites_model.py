import sqlalchemy as sa
from datetime import datetime
from src.config.model_base import Base, ModelBase

class EmitesModel(Base, ModelBase):
    __tablename__: str = "emites"
    cantidad: sa.Column = sa.Column(sa.Integer, nollable = False)
    cantidad_emitida: sa.Column = sa.Column(sa.Integer, nollable = False)
    producto_id: sa.Column = sa.Column(sa.Integer, sa.ForeignKey('productos.id'), nullable=False)
    venta_id:sa.Column = sa.Column(sa.Integer, sa.ForeignKey('productos.id'), nullable=False)
    created_at: sa.Column = sa.Column(sa.DateTime, default=datetime.now(), nullable=False)
    updated_at: sa.Column = sa.Column( sa.DateTime, default=datetime.now(), nullable=False)
    