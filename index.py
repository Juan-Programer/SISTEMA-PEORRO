from tkinter import *
from tkinter import ttk
from src.screen.login_screen import LoginScreen

"""
def __init__(self, window):
        self.wind = window
        self.wind.title('CONTROL DE VENTAS Y INVENTARIO')

        #CREANDO UN FRAME CONTAINER
        frame = LabelFrame(self.wind, text = 'Registre un nuevo Producto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #Nombre de Entrada
        Label(frame, text  = 'Nombre:').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.grid(row = 1, column = 1)

        #Precio de entrada
        Label(frame, text = 'Precio:').grid(row = 2, column = 0)
        self.precio = Entry(frame)
        self.precio.grid(row = 2, column = 1)

        #Boton agregar producto
        ttk.Button(frame, text = 'Guardar Producto').grid(row = 3, columnspan = 2, sticky = W + E)

        #Tabla
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#1', text = 'Precio', anchor = CENTER)

        self (get_productos)

def run_query (self, query, parameters = ()):
    with sqlite3.connect(self.db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result

"""

if __name__ == '__main__':
	window = Tk()
	login: LoginScreen = LoginScreen(window)
	window.mainloop()




