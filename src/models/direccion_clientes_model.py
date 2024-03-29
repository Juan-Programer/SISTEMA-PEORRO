import sqlalchemy as sa
from datetime import datetime
from src.config.model_base import Base, ModelBase

class Direccion_clientesModel(Base, ModelBase):
    __tablename:str = "direccion_clientes"
    calle: sa.Column = sa.Column(sa.String, nullable=False)
    sector: sa.Column = sa.Column(sa.String, nullable=False)
    comuna: sa.Column = sa.Column(sa.String, nullable=False)
    numero: sa.Column = sa.Column(sa.String, nullable=False)
    cuidad: sa.Column = sa.Column(sa.String, nullable=False)
    cliente_id: sa.Column = sa.Column(sa.Integer, sa.ForeignKey('clientes.id'), nullable=False)
    created_at: sa.Column = sa.Column( sa.DateTime, default = datetime.now(), nullable = False )
    updated_at: sa.Column = sa.Column( sa.DateTime, default = datetime.now(), nullable = False )
