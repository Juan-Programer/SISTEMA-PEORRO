import sqlalchemy as sa
from src.config.model_base import Base, ModelBase

class EmpleadoModel(Base, ModelBase):
	__tablename__:str = "empleados"
	id: sa.Column = sa.Column( sa.Integer, primary_key = True)
	usuario: sa.Column = sa.Column( sa.String(50), nullable = False)
	contrasena: sa.Column = sa.Column( sa.String(250),  nullable = False)
	created_at: sa.Column = sa.Column( sa.DateTime, nullable = False )
	updated_at: sa.Column = sa.Column( sa.DateTime, nullable = False )
