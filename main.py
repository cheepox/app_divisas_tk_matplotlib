import tkinter as tk
from funciones_widgets import func_widgets
from function_request import funciones
import requests


ventana = tk.Tk()

ventana.title("app")
ventana.geometry("400x800")

widget = func_widgets(ventana)
widget.actualizar_label()
ventana.mainloop()