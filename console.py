from src.services.categoria_service import CategoriaService

class ConsoleApp():

	def run(self):
		try:
			id: str = input("Ingrese el identificador de formato(ID): ")
			
			categoria_service: CategoriaService = CategoriaService()
			categoria_service.eliminar( categoria_id =id)

		except ValueError as e:
			print(e)
			print("no se pudo crear el usuario")

if __name__ == '__main__':
	console: ConsoleApp = ConsoleApp()
	console.run()
