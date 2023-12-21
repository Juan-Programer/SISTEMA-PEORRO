import sqlalchemy as sa
from datetime import datetime
from src.config.model_base import Base, ModelBase

class ProductosModel(Base, ModelBase):
    __tablename__:str = "productos"
    id: sa.Column = sa.Column( sa.Integer, primary_key = True)
    nombre: sa.Column = sa.Column(sa.String, nullable=False)
    precio_compra: sa.Column = sa.Column (sa.Numeric(10,2), nullable=False)
    precio_venta: sa.Column = sa.Column(sa.Numeric(10,2), nullable=False)
    descripcion: sa.Column = sa.Column(sa.String, nullable = False)
    producto_inventario: sa.Column = sa.Column(sa.Integer, nullable = False)
    categoria_id: sa.Column = sa.Column(sa.Integer, sa.ForeignKey('categorias.id'), nullable = False)
    created_at: sa.Column = sa.Column( sa.DateTime, default=datetime.now(), nullable=False)
    updated_at: sa.Column= sa.Column( sa.DateTime, default = datetime.now(), nullable=False)