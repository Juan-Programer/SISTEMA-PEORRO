import sqlalchemy as sa
from datetime import datetime
from src.config.model_base import Base, ModelBase

class CategoriaModel(Base, ModelBase):
    __tablename__:str = "categorias"
    id: sa.Column = sa.Column( sa.Integer, primary_key = True)
    nombre: sa.Column = sa.Column(sa.String(45), nullable=False)
    created_at: sa.Column = sa.Column( sa.DateTime, default = datetime.now(), nullable = False )
    updated_at: sa.Column = sa.Column( sa.DateTime, default = datetime.now(), nullable = False )