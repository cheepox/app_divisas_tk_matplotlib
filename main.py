import tkinter as tk
from funciones_widgets import func_widgets
from funciones_request import funciones

def cerrar_aplicacion():
    ventana.quit()
    ventana.destroy()

ventana = tk.Tk()

ventana.title("app")
ventana.geometry("400x350")

widget = func_widgets(ventana)

widget.actualizar_label()

ventana.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)

ventana.mainloop()