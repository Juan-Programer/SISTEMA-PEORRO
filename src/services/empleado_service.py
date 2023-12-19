from src.models.empleado_model import EmpleadoModel
from src.util.password_encrypt import PasswordEncrypt
from src.config.session_database import SessionDatabase

class EmpleadoService():

	# function that login username
	def login(self, username: str, password: str) -> EmpleadoModel:
		session: SessionDatabase = SessionDatabase()

		try:

			user = session.query(EmpleadoModel)\
				.filter(EmpleadoModel.usuario == username)\
				.first()

			if user == None:
				return None

			hashed: PasswordEncrypt = PasswordEncrypt(hashed = user.contrasena)
			if hashed.compare(password) == False:
				return None

			return user
		
		finally:
			session.close()
