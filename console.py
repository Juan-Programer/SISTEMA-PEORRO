from sqlalchemy import desc
from src.services.producto_service import ProductoService

class ConsoleApp():

	def run(self):
		try:
			producto_id: int = int (input("Ingrese el identificador de formato"))
			producto_nuevo_nombre: str = input("Ingrese el nombre del producto: ")
			nuevo_precio_compra: float= float(input("Ingrese el precio de compra del producto: "))
			nuevo_precio_venta:  float= float(input("Ingrese el precio de venta del producto: "))
			nueva_descripcion: str = input("Ingrese la descripcion del producto: ")
			nuevo_producto_inventario: int = int (input("Ingrese el numero de productos en el inventario: "))
			categoria_id: int = int(input("Ingrese la categoria.id: "))

			producto_service: ProductoService = ProductoService()

			producto_service.edit(
				producto_id= producto_id,
				producto_nuevo_nombre= producto_nuevo_nombre,
				nuevo_precio_compra=nuevo_precio_compra,
				nuevo_precio_venta=nuevo_precio_venta, 
				nueva_descripcion=nueva_descripcion, 
				nuevo_producto_inventario=nuevo_producto_inventario,
				categoria_id=categoria_id
			)

		except ValueError as e:
			print(e)
			print("no se pudo crear el usuario")

if __name__ == '__main__':
	console: ConsoleApp = ConsoleApp()
	console.run()
