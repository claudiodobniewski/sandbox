import tkinter as tk
from tkinter import ttk

# Mantener la variable que controla el icono
uno_o_dos = 1

ventana = tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("400x300")

# Precargar iconos y guardar referencias en la ventana para evitar que sean garbage-collected
icons = {
    1: tk.PhotoImage(file="iconos/1.png"),
    2: tk.PhotoImage(file="iconos/2.png")
}
ventana._icons = icons  # referencia segura

# Establecer icono inicial según uno_o_dos
ventana.iconphoto(True, ventana._icons.get(uno_o_dos))

def mostrar_mensaje():
    global uno_o_dos
    # Incrementa y hace wrap a 1..2
    uno_o_dos += 1
    if uno_o_dos > 2:
        uno_o_dos = 1
    # Actualiza el icono usando la imagen precargada
    ventana.iconphoto(True, ventana._icons[uno_o_dos])
    # Actualiza etiqueta de estado
    estado_label.config(text=f"Icono actual: {uno_o_dos}")

# Crear un label para mostrar el estado actual (nuevo, no intrusivo)
estado_label = tk.Label(ventana, text=f"Icono actual: {uno_o_dos}")
estado_label.pack(pady=(10, 0))

boton_saludo = tk.Button(ventana, text="Haz clic", command=mostrar_mensaje)

boton_saludo.pack(pady=20)

ventana.mainloop()