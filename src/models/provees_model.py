import sqlalchemy as sa
from datetime import datetime
from src.config.model_base import Base, ModelBase

class ProveeModel(Base, ModelBase):
    __tablename__:str = "provees"
    proveedor_id: sa.Column = sa.Column(sa.Integer, sa.ForeignKey('proveedores.id'), nullable=False)
    producto_id: sa.Column = sa.Column (sa.Integer, sa.ForeignKey('productos.id'), nullable=False)
    created_at:sa.Column = sa.Column(sa.DateTime, default=datetime.now(), nullable=False)
    updated_at:sa.Column = sa.Column(sa.DateTime, default=datetime.now(), nullable=False)
    

    