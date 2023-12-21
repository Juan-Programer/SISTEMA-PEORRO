from unicodedata import numeric
from sqlalchemy import desc
from src.services.producto_service import ProductoService

class ConsoleApp():

	def run(self):
		try:
			nombre: str = input("Ingrese el nombre del producto: ")
			precio_compra: float= input("Ingrese el precio de compra del producto: ")
			precio_venta:  float= input("Ingrese el precio de venta del producto: ")
			descripcion: str = input("Ingrese la descripcion del producto")
			producto_inventario:str=int (input("Ingrese el numero de productos en el inventario"))
			categoria_id: str = int(input("Ingrese la categoria.id "))

			
			producto_service: ProductoService = ProductoService()
			producto_service.create( nombre=nombre, 
						     precio_compra=precio_compra,
							 precio_venta=precio_venta, 
							 descripcion=descripcion, 
							 producto_inventario=producto_inventario,
						     categoria_id=categoria_id)

		except ValueError as e:
			print(e)
			print("no se pudo crear el usuario")

if __name__ == '__main__':
	console: ConsoleApp = ConsoleApp()
	console.run()
