from src.models.categorias_model import CategoriaModel
from src.config.session_database import SessionDatabase
from sqlalchemy import func
from datetime import datetime

class CategoriaService():

    # Crear una categoría de productos.
    def create(self, nombre:str ) -> CategoriaModel:
        session: SessionDatabase = SessionDatabase()

        try:
            # Verificar si ya existe una categoría con el mismo nombre
            existing_categoria = session.query(CategoriaModel).filter(func.upper(CategoriaModel.nombre) == func.upper(nombre)).first()
            if existing_categoria:
                raise ValueError("Ya existe una categoria con este mismo nombre")

            categoria: CategoriaModel = CategoriaModel(
                nombre=nombre
            )

            session.add(categoria)

            session.commit()

            return categoria
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    # Editar una categoría por su identificador único
    def edit(self, categoria_id: int, nuevo_nombre: str) -> CategoriaModel:
        session: SessionDatabase = SessionDatabase()

        try:
            categoria = session.query(CategoriaModel).filter_by(id=categoria_id).first()
            if not categoria:
                raise ValueError("La categoría no existe")

            # Verificar si ya existe una categoría con el nuevo nombre
            existing_categoria = session.query(CategoriaModel).filter(func.upper(CategoriaModel.nombre) == func.upper(nuevo_nombre)).first()
            if existing_categoria:
                raise ValueError("Ya existe una categoría con el nuevo nombre")

            categoria.nombre = nuevo_nombre
            categoria.updated_at = datetime.now()
            session.commit()

            return categoria
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

            #Eliminar una categoria
    def eliminar(self, categoria_id: int) -> CategoriaModel:
        session: SessionDatabase = SessionDatabase()

        try:
            categoria = session.query(CategoriaModel).filter_by(id=categoria_id).first()
            if not categoria:
                raise ValueError("No hay ninguna categoria para elimanar de este tipo")
            
            session.delete(categoria)

            session.commit()

            return categoria
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

            
            
            
                    


        
    

