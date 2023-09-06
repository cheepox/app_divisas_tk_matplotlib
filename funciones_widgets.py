import tkinter as tk
from funciones_request import funciones

class func_widgets:


    def __init__(self, ventana):
        self.ventana = ventana

        self.titulo_Tipo_Moneda = tk.Label(ventana, text= "DOLAR BLUE")

        self.etiqueta_valor_compra = tk.Label(ventana, text="")
        self.etiqueta_subtitulo_compra = tk.Label(ventana, text="Valor compra")

        self.etiqueta_subtitulo_venta = tk.Label(ventana,text= "Valor Venta")
        self.etiqueta_valor_venta = tk.Label(ventana,text = "")

        #entrada de texto
        self.etiqueta_texto = tk.Label(ventana, text="Ingrese la cantidad de dias a graficar.\n!no mas de 8¡")
        self.entrada_texto = tk.Entry(ventana,text = "Ingrese cantidad de dias", width = 15)

        #Botones guardar grafico y mostrarlo
        self.boton_guardar = tk.Button(ventana, text = "GUARDAR GRAFICO",command=self.guardar_grafico)

        self.boton_mostrar = tk.Button(ventana,text="MOSTRAR GRAFICO",command = self.mostrar_grafico)
        #ACTIVACION DE LOS WIDGETS
        self.titulo_Tipo_Moneda.pack()

        self.etiqueta_subtitulo_compra.pack()
        self.etiqueta_valor_compra.pack()

        self.etiqueta_subtitulo_venta.pack()
        self.etiqueta_valor_venta.pack()

        #entrada de texto
        self.etiqueta_texto.pack()
        self.entrada_texto.pack()
        #boton guardar grafico
        self.boton_guardar.pack() 
        self.boton_mostrar.pack()

        self.actualizar_label()

    def actualizar_label(self):
        compra = funciones.Valor_promedio()
        venta = funciones.Valor_venta()

        self.etiqueta_valor_venta.config(text = venta)
        self.etiqueta_valor_compra.config(text=compra)


    def guardar_grafico(self):
        dias_ingresados = 1 + int(self.entrada_texto.get())
        funciones.guardar_Grafico(dias_ingresados)
    
    def mostrar_grafico(self):
        dias_ingresados = 1 + int(self.entrada_texto.get())
        funciones.mostrar_Grafico(dias_ingresados)
    