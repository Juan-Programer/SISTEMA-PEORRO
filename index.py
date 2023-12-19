from tkinter import *
from tkinter import ttk
from src.screen.login_screen import LoginScreen





if __name__ == '__main__':
	window = Tk()
	login: LoginScreen = LoginScreen(window)
	window.mainloop()




