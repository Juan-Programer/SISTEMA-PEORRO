import sqlalchemy as sa
from datetime import datetime
from src.config.model_base import Base, ModelBase

class VentasModel(Base, ModelBase):
    __tablename__:str = "ventas"
    id: sa.Column = sa.Column(sa.Integer, primary_key = True)
    fecha : sa.Column = sa.Column(sa.DateTime, default = datetime.now(), nullable=False)
    productos_vendidos : sa.Column = sa.Column(sa.String(45), nullable=False)
    precio_de_venta : sa.Column = sa.Column(sa.Numeric(45), nullable=False)
    created_at : sa.Column = sa.Column(sa.DateTime, default=datetime.now(), nullable=False)
    updated_at: sa.Column = sa.Column(sa.DateTime, default=datetime.now(), nullable=False)
    cliente_id : sa.Column = sa.Column(sa.Integer, sa.ForeignKey('clientes.id'), nullable=False)
    empleado_id : sa.Column = sa.Column(sa.Integer, sa.ForeignKey('empleados.id'), nullable=False)
