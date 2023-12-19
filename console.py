from src.services.empleado_service import EmpleadoService

class ConsoleApp():

	def run(self):
		username: str = input("ingrese su usuario: ")
		password: str = input("ingresar contrasenia: ")
		empleado_service: EmpleadoService = EmpleadoService()
		user = empleado_service.login(username, password)

		if user == None:
			print("La contraseña o usuario es incorrecta")
		else:
			print("ha iniciado sesion correctamente")
			print(user)

if __name__ == '__main__':
	console: ConsoleApp = ConsoleApp()
	console.run()
