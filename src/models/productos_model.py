import sqlalchemy as sa
from datetime import datetime
from src.config.model_base import Base, ModelBase

class ProductosModel(Base, ModelBase):
    __tablename__:str = "productos"
    id: sa.Column = sa.Column( sa.Integer, primary_key = True)
    nombre: sa.Column = sa.Column(sa.String(45), nullable=False)
    precio_compra: sa.Column = sa.Column (sa.Numeric(10,2), nullable=False)
    precio_venta: sa.Column = sa.Column(sa.Numeric(10,2), nullable=False)
    descripcion: sa.Column = sa.Column(sa.String, nullable = False)
    producto_inventario: sa.Column = sa.Column(sa.Integer, nullable = False)
    categoria_id: sa.Column = sa.Column(sa.Integer, sa.ForeignKey('categorias'), nullable = False)
    sa.Column('created_at', sa.DateTime, default=datetime.now(), nullable=False),
    sa.Column('updated_at', sa.DateTime, default = datetime.now(), nullable=False)