from src.services.empleado_service import EmpleadoService

class ConsoleApp():

	def run(self):
		try:

			username: str = input("ingrese su usuario: ")
			password: str = input("ingresar contrasenia: ")
			cedula: str = input("ingresar cedula: ")
			nombre: str = input("ingresar nombre: ")
			apellido: str = input("inpurt apellido")

			empleado_service: EmpleadoService = EmpleadoService()
			empleado_service.create(usuario=username, contrasena=password, cedula=cedula,nombre=nombre, apellido=apellido)
		except ValueError as e:
			print(e)
			print("no se pudo crear el usuario")

if __name__ == '__main__':
	console: ConsoleApp = ConsoleApp()
	console.run()
