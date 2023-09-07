import tkinter as tk
from funciones_request import funciones

class func_widgets:


    def __init__(self, ventana):
        self.ventana = ventana

        self.titulo_Tipo_Moneda = tk.Label(ventana, text= "DOLAR BLUE",font =("Helvetica",13,"bold"))

        self.etiqueta_valor_compra = tk.Label(ventana, text="",font=("Helvetica",11,"bold"))
        self.etiqueta_subtitulo_compra = tk.Label(ventana, text="Valor compra",font=("Helvetica",10))

        self.etiqueta_subtitulo_venta = tk.Label(ventana,text= "Valor Venta",font=("Helvetica",10))
        self.etiqueta_valor_venta = tk.Label(ventana,text = "",font=("Helvetica",11,"bold"))

        #entrada de texto
        self.etiqueta_texto = tk.Label(ventana, text="Ingrese la cantidad de dias a graficar.\n!no mas de 8¡")
        self.entrada_texto = tk.Entry(ventana,text = "Ingrese cantidad de dias", width = 15)

        #Botones guardar grafico y mostrarlo
        self.boton_guardar = tk.Button(ventana, text = "GUARDAR GRAFICO",command=self.guardar_grafico)

        self.boton_mostrar = tk.Button(ventana,text="MOSTRAR GRAFICO",command = self.mostrar_grafico)
        #Etiqueta de ultima actualizacion
        self.subtitulo_last_update = tk.Label(ventana,text ="Ultima actualizacion")
        self.etiqueta_last_update = tk.Label(ventana,text ="" )
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

        #ultima actualizacion
        self.subtitulo_last_update.pack()
        self.etiqueta_last_update.pack()

        self.actualizar_label()

    def actualizar_label(self):
        compra = funciones.Valor_compra()
        venta = funciones.Valor_venta() 
        last_update = funciones.ultima_actualizacion()

        self.etiqueta_valor_venta.config(text = venta)
        self.etiqueta_valor_compra.config(text=compra)
        self.etiqueta_last_update.config(text=last_update)


    def guardar_grafico(self):
        if self.entrada_texto.get() == "":
            dias_ingresados = 1 
        else:
            dias_ingresados = 1 + int(self.entrada_texto.get())
        funciones.guardar_Grafico(dias_ingresados)
    
    def mostrar_grafico(self):
        if self.entrada_texto.get() == "":
            dias_ingresados = 1 
        else:
            dias_ingresados = 1 + int(self.entrada_texto.get())
        funciones.mostrar_Grafico(dias_ingresados)
    