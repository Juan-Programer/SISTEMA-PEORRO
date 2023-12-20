from sqlalchemy import func
from src.models.empleado_model import EmpleadoModel
from src.util.password_encrypt import PasswordEncrypt
from src.config.session_database import SessionDatabase

class EmpleadoService():

	# crear un empleado
	def create(self, usuario: str, contrasena: str, cedula: str, nombre: str, apellido: str) -> EmpleadoModel:
		session: SessionDatabase = SessionDatabase()

		try:
			hashed: PasswordEncrypt = PasswordEncrypt(contrasena)

			user: EmpleadoModel = session.query(EmpleadoModel)\
				.filter(func.upper(EmpleadoModel.usuario) == func.upper(usuario))\
				.first()

			if user != None:
				raise ValueError("El usuario existe intente con otro usuario")

			empleado: EmpleadoModel = EmpleadoModel(
				usuario=usuario,
				nombre=nombre,
				apellido=apellido,
				contrasena=hashed.get_hash(),
				cedula=cedula
			)

			session.add(empleado)

			created: EmpleadoModel = session.query(EmpleadoModel)\
				.filter(EmpleadoModel.usuario == usuario)\
				.first()

			session.commit()
			return created
		finally:
			session.close()

	# function that login username
	def login(self, username: str, password: str) -> EmpleadoModel:
		session: SessionDatabase = SessionDatabase()

		try:
			user = session.query(EmpleadoModel)\
				.filter(func.upper(EmpleadoModel.usuario) == func.upper(username))\
				.first()

			if user == None:
				return None

			hashed: PasswordEncrypt = PasswordEncrypt(hashed = user.contrasena)
			if hashed.compare(password) == False:
				return None

			return user

		finally:
			session.close()
