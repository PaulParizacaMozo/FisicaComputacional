import tkinter as tk
from tkinter import messagebox
import math

# Función para validar si el campo está vacío
def validar_campo_vacio(campo):
    if campo.strip() == "":
        return False
    return True

# Función para calcular la velocidad orbital
def calcular_velocidad_orbital():
    try:
        radio_str = entry_radio.get()
        periodo_str = entry_periodo.get()
        
        # Validación de campos vacíos
        if not validar_campo_vacio(radio_str) or not validar_campo_vacio(periodo_str):
            raise ValueError("Todos los campos son obligatorios.")
        
        # Conversión a float
        radio = float(radio_str)
        periodo = float(periodo_str)
        
        # Validación de valores no negativos o cero
        if radio <= 0 or periodo <= 0:
            raise ValueError("El radio y el periodo deben ser mayores que cero.")
        
        # Fórmula para la velocidad orbital v = 2 * pi * r / T
        velocidad = (2 * math.pi * radio) / periodo
        label_resultado_velocidad.config(text=f"Velocidad orbital: {velocidad:.2f} m/s")
    
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {str(e)}")

# Función para calcular la longitud de la órbita
def calcular_longitud_orbita():
    try:
        radio_str = entry_radio.get()
        
        # Validación de campo vacío
        if not validar_campo_vacio(radio_str):
            raise ValueError("El campo de radio es obligatorio.")
        
        # Conversión a float
        radio = float(radio_str)
        
        # Validación de valor no negativo o cero
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero.")
        
        # Fórmula para la longitud de la órbita (circunferencia): L = 2 * pi * r
        longitud_orbita = 2 * math.pi * radio
        label_resultado_orbita.config(text=f"Longitud de la órbita: {longitud_orbita:.2f} m")
    
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {str(e)}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Velocidad Orbital y Órbita")

# Sección para los datos de entrada
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

label_radio = tk.Label(frame_entrada, text="Radio de la órbita (m):")
label_radio.grid(row=0, column=0)
entry_radio = tk.Entry(frame_entrada)
entry_radio.grid(row=0, column=1)

label_periodo = tk.Label(frame_entrada, text="Periodo orbital (s):")
label_periodo.grid(row=1, column=0)
entry_periodo = tk.Entry(frame_entrada)
entry_periodo.grid(row=1, column=1)

# Botones para realizar los cálculos
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton_calcular_velocidad = tk.Button(frame_botones, text="Calcular Velocidad Orbital", command=calcular_velocidad_orbital)
boton_calcular_velocidad.grid(row=0, column=0, padx=5)

boton_calcular_orbita = tk.Button(frame_botones, text="Calcular Longitud de la Órbita", command=calcular_longitud_orbita)
boton_calcular_orbita.grid(row=0, column=1, padx=5)

# Resultados
frame_resultado = tk.Frame(ventana)
frame_resultado.pack(pady=10)

label_resultado_velocidad = tk.Label(frame_resultado, text="Velocidad orbital: ")
label_resultado_velocidad.grid(row=0, column=0)

label_resultado_orbita = tk.Label(frame_resultado, text="Longitud de la órbita: ")
label_resultado_orbita.grid(row=1, column=0)

# Aseguramos que los labels se actualicen correctamente
label_resultado_velocidad.config(text="")
label_resultado_orbita.config(text="")

# Iniciar la ventana principal
ventana.mainloop()
