import tkinter as tk

limite_fabricacion_diaria=10000
churros_disponibles=limite_fabricacion_diaria

'''def comparar_churros(churros_encargados):
    if churros_encargados <= limite_fabricacion_diaria:
        return "Se pueden fabricar todos los churros encargados."
    else:
        return "No se pueden fabricar todos los churros encargados."
'''

def comparar_churros_bool(churros_encargados):
    return churros_encargados <= churros_disponibles
        
def estado_del_pedido():
    estado = comparar_churros_bool(int(campo_texto_2.get()))
    resultado ="ACEPTADO" if estado else "RECHAZADO"
    info_estado_pedido.set(resultado)

    return estado

def actualizar_churros(churros_encargados):
    global churros_disponibles
    churros_disponibles = churros_disponibles-churros_encargados

def imprimir_consola(fabricacion,churros_encargados):
    print("Fabricacion Diaria:", fabricacion)
    print("Pedido de Churros:", churros_encargados)
    print("Churros Disponibles:", churros_disponibles)
    print("Estado del Pedido:", info_estado_pedido.get())

def mostrar_churros_disponibles():
    if estado_del_pedido():
        actualizar_churros(int(campo_texto_2.get()))
        texto4.config(text=churros_disponibles)
    
def verificar_clic():
    mostrar_churros_disponibles()
    imprimir_consola(campo_texto_1.get(),campo_texto_2.get())


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("QChurreria-Undav")

fabricacion = tk.IntVar()
fabricacion.set(limite_fabricacion_diaria)

info_estado_pedido = tk.StringVar()
info_estado_pedido.set("SIN DATOS")

# Configurar el tamaño de la ventana
ventana.geometry("340x180")  # Anchura x Altura

# Crear la etiqueta de texto
texto1 = tk.Label(ventana, text="Fabricacion Diaria:")
texto1.grid(row=0, column=0, padx=10, pady=10)

texto2 = tk.Label(ventana, text="Pedido de Churros:")
texto2.grid(row=1, column=0, padx=10, pady=10)

texto3 = tk.Label(ventana, text="Churros Disponibles:")
texto3.grid(row=2, column=0, padx=10, pady=10)

texto4 = tk.Label(ventana, text=churros_disponibles)
texto4.grid(row=2, column=1, padx=10, pady=10)

texto5 = tk.Label(ventana,textvariable=info_estado_pedido)
texto5.grid(row=3, columnspan=3, padx=5, pady=10)

# Crear el botón

boton1 = tk.Button(ventana, text="Verificar", command=verificar_clic)
boton1.grid(row=0, column=3, padx=10, pady=10)

# Crear el campo de texto editable
campo_texto_1 = tk.Entry(ventana,textvariable=fabricacion,state="readonly")
campo_texto_1.grid(row=0, column=1, padx=5, pady=10)

campo_texto_2 = tk.Entry(ventana)
campo_texto_2.grid(row=1, column=1, padx=5, pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()