from src.models.categorias_model import CategoriaModel
from src.models.productos_model import ProductosModel
from datetime import datetime
from src.config.session_database import SessionDatabase
from sqlalchemy import func

class ProductoService():

    #Crear un producto
    def create(self, nombre:str, precio_compra:float, precio_venta:float, descripcion:str, producto_inventario: int, categoria_id: int ) -> ProductosModel:
        session: SessionDatabase = SessionDatabase()

        try:
            # Crear un producto y ver si ya es existente.
            existing_producto = session.query(ProductosModel)\
                .filter(func.upper(ProductosModel.nombre) == func.upper(nombre))\
                .first()
            

            if existing_producto:
                raise ValueError("Ya existe este producto en esta base de datos")


            category = session.query(CategoriaModel)\
                .filter(CategoriaModel.id == categoria_id)\
                .first()
            
            if not category:
                raise ValueError("la categoria seleccionada no existe")

            producto: ProductosModel = ProductosModel(
                nombre=nombre,
                precio_compra = precio_compra,
                precio_venta=precio_venta,
                descripcion = descripcion,
                producto_inventario=producto_inventario,
                categoria_id = category.id
            )

            session.add(producto)

            created: ProductosModel = session.query(ProductosModel)\
                .filter(ProductosModel.nombre == nombre)\
                .first()
            
            session.commit()
            
            
            return created
        finally:
            session.close()

            #Editar un producto utilizando su nombre.
    def edit(
        self, 
        producto_id: int, 
        producto_nuevo_nombre:str,
        nuevo_precio_compra:float,
        nuevo_precio_venta:float,
        nuevo_producto_inventario:int,
        nueva_descripcion: str,
        categoria_id: int
    ) -> ProductosModel:

        session: SessionDatabase = SessionDatabase() 
        
        try:
           
            
            category = session.query(CategoriaModel)\
                .filter(CategoriaModel.id == categoria_id)\
                .first()
            
            if not category:
                raise ValueError("la categoria seleccionada no existe")
            
            producto = session.query(ProductosModel)\
                .filter(ProductosModel.id == producto_id)\
                .first()
        
            if not producto:
                raise ValueError("Este producto no se encuentra registrado")
        
            #Verificar si ya existe el producto
            existing_producto = session.query(ProductosModel)\
                .filter( ProductosModel.id != producto_id)\
                .filter(func.upper(ProductosModel.nombre) == func.upper(producto_nuevo_nombre))\
                .first()

            if existing_producto:
                raise ValueError("Ya existe un producto con este nombre en el sistema")
            
        
            producto.nombre = producto_nuevo_nombre
            producto.precio_compra = nuevo_precio_compra
            producto.precio_venta = nuevo_precio_venta
            producto.descripcion = nueva_descripcion
            producto.inventario = nuevo_producto_inventario
            producto.updated_at = datetime.now ()

            session.add(producto)

            session.commit()

            return producto
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()