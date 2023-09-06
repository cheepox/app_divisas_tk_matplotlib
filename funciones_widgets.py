import tkinter as tk
from function_request import funciones


class func_widgets:
    def __init__(self, ventana):
        self.ventana = ventana
        self.etiqueta_valor_compra = tk.Label(ventana, text="")
        self.etiqueta_subtitulo = tk.Label(ventana, text="Valor compra")
        self.etiqueta_subtitulo.pack()
        self.etiqueta_valor_compra.pack()
        self.actualizar_label()

    def actualizar_label(self):
        compra = funciones.Valor_compra()
        self.etiqueta_valor_compra.config(text=compra)
        self.ventana.after(3000, self.actualizar_label)