# from PIL import Image, ImageTk
from src.screen.base_screen import BaseScreen
from src.models.empleado_model import EmpleadoModel
from src.services.empleado_service import EmpleadoService
from tkinter import Tk,Label,Button,Entry,Frame,messagebox


class LoginScreen(BaseScreen):
    def render(self):
        self.window.geometry("400x700")
        self.window.title("Mi primer login")

        fondo = "#88FFB4"

    	#--------------------------------------------
    	#--------------------parde de frame----------
    	#--------------------------------------------

        self.frame_superior = Frame(self.window)
        self.frame_superior.configure(bg=fondo)
        self.frame_superior.pack(fill="both", expand = True)

        self.frame_inferior = Frame(self.window)
        self.frame_inferior.configure(bg=fondo)
        self.frame_inferior.pack(fill="both", expand = True)

        self.frame_inferior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(0, weight=1)

        #
        #-------------------------------------
        #

        self.titulo = Label(self.frame_superior,
                            text="Login",
                            font=("Calisto MT", 36, "bold" ),
                            bg=fondo)
        self.titulo.pack(side="top", pady=20)

        #
        #
        #

        # self.img = Image.open("imagenes/usuario.png")
        # self.omg = self.img.resize((150,120))
        # self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_superior, bg = fondo)
        self.fondo.pack(expand=True, fill="both", side="top")

        #
        #
        #

        self.label_usuario = Label(self.frame_inferior,
                                   text="Usuario",
                                   font= ("Arial",18),
                                   bg=fondo,
                                   fg="black")
        self.label_usuario.grid(row=0, column=0, padx=10, sticky="e")

        self.entry_usuario = Entry(self.frame_inferior,
                                   bd=0,
                                   width=14,
                                   font=("Arial", 18))
        self.entry_usuario.grid(row = 0, column=1, columnspan=3, padx=5, sticky="w")

        self.label_contraseña = Label(self.frame_inferior,
                                   text="Contraseña",
                                   font= ("Arial",18),
                                   bg=fondo,
                                   fg="black")
        self.label_contraseña.grid(row=1, column=0, padx=10, sticky="e")

        self.entry_contraseña= Entry(self.frame_inferior,
                                   bd=0,
                                   width=14,
                                   font=("Arial",18),
                                   show="*")

        self.entry_contraseña.grid(row = 1, column=1, columnspan=3, padx=5, sticky="w")

        self.boton_ingresar = Button (self.frame_inferior,
                                      text="Ingresar",
                                      width=16,
                                      font=("Arial", 12),
                                      command=self.entrar)
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, pady=35)


    def entrar(self):
        nombre = self.entry_usuario.get()
        contra = self.entry_contraseña.get()
        empleado_service: EmpleadoService = EmpleadoService()
        user: EmpleadoModel = empleado_service.login(nombre, contra)

        if user != None:
            messagebox.showinfo("Acceso Correcto", "Has Ingresado")
        else:
            messagebox.showinfo("Acceso Incorrecto", "La contraseña y el usuario no coinciden")
