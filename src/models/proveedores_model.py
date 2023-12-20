import sqlalchemy as sa
from datetime import datetime
from src.config.model_base import Base, ModelBase

class ProveedoresModel(Base, ModelBase):
    __tablename__: str= "proveedores"
    id: sa.Column = sa.Column( sa.Integer, primary_key = True)
    nombre_de_proveedor: sa.Column = sa.Column( sa.String(45), nullable=False)
    rif: sa.Column = sa.Column( sa.String(60), nullable=False)
    telefono: sa.column = sa.Column( sa.String(60), nullable=False)
    correo_electronico: sa.Column = sa.Column( sa.String(60), nullable=False)
    created_at: sa.Column = sa.Column(sa.DateTime, default=datetime.now(), nullable=False)
    updated_at: sa.Column = sa.Column(sa.DateTime, default=datetime.now(), nullable=False)