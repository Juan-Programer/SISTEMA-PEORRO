from src.models.productos_model import ProductosModel
from src.config.session_database import SessionDatabase
from sqlalchemy import func

class ProductoService():

    #Crear un producto
    def create(self, nombre:str, precio_compra:float, precio_venta:float, descripcion:str, producto_inventario: int, categoria_id: int ) -> ProductosModel:
        session: SessionDatabase = SessionDatabase()

        try:
            #Crear un producto y ver si ya es existente.
            existing_producto = session.query(ProductosModel). filter(func.upper(ProductosModel.nombre) == func.upper(nombre)).first()
            if existing_producto:
                raise ValueError ("Ya existe este producto en esta base de datos")
            
            producto: ProductosModel = ProductosModel(
                nombre=nombre,
                precio_compra = precio_compra,
                precio_venta=precio_venta,
                descripcion = descripcion,
                producto_inventario=producto_inventario,
                categoria_id = categoria_id 
            )

            session.add(producto)

            created: ProductosModel = session.query(ProductosModel)\
            .filter(ProductosModel.nombre == nombre)\
            .first()
            session.commit()
            return created
        finally:
            session.close()



    
