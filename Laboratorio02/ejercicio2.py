import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Función para calcular la fuerza
def calcular_fuerza():
    try:
        # Obtener valores de las entradas
        masa_str = entry_masa.get()
        vi_str = entry_vi.get()
        vf_str = entry_vf.get()
        tiempo_str = entry_tiempo.get()

        # Validación de campos vacíos
        if not masa_str or not vi_str or not vf_str or not tiempo_str:
            raise ValueError("Todos los campos son obligatorios.")

        # Conversión a float
        masa = float(masa_str)
        vi = float(vi_str)
        vf = float(vf_str)
        tiempo = float(tiempo_str)

        # Validación de valores no negativos o cero
        if tiempo <= 0 or masa <= 0:
            raise ValueError("El tiempo y la masa deben ser mayores que cero.")

        # Cálculo de la aceleración
        a = (vf - vi) / tiempo
        
        # Cálculo de la fuerza F = m * a
        fuerza = masa * a

        # Mostrar los resultados en la interfaz
        label_resultado_fuerza.config(text=f"Fuerza ejercida: {fuerza:.2f} N")
        label_resultado_aceleracion.config(text=f"Aceleración: {a:.2f} m/s²")

        # Graficar el proceso de fuerza a lo largo del tiempo
        graficar_proceso_fuerza(tiempo, fuerza)

    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {str(e)}")

# Función para graficar el proceso de fuerza
def graficar_proceso_fuerza(t, f):
    # Tiempos para graficar desde 0 hasta t con un punto cada segundo
    tiempos = np.linspace(0, t, num=int(t)+1)
    fuerzas = np.full_like(tiempos, f)  # Fuerza constante en el intervalo de tiempo

    plt.figure(figsize=(8, 6))
    plt.plot(tiempos, fuerzas, marker='o', linestyle='-', color='blue')
    plt.title("Fuerza Aplicada a lo largo del Tiempo")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Fuerza (N)")
    plt.grid(True)
    plt.show()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Fuerza y Gráfica de Fuerza")

# Sección para los datos de entrada
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

label_masa = tk.Label(frame_entrada, text="Masa (kg):")
label_masa.grid(row=0, column=0)
entry_masa = tk.Entry(frame_entrada)
entry_masa.grid(row=0, column=1)

label_vi = tk.Label(frame_entrada, text="Velocidad inicial (m/s):")
label_vi.grid(row=1, column=0)
entry_vi = tk.Entry(frame_entrada)
entry_vi.grid(row=1, column=1)

label_vf = tk.Label(frame_entrada, text="Velocidad final (m/s):")
label_vf.grid(row=2, column=0)
entry_vf = tk.Entry(frame_entrada)
entry_vf.grid(row=2, column=1)

label_tiempo = tk.Label(frame_entrada, text="Tiempo (s):")
label_tiempo.grid(row=3, column=0)
entry_tiempo = tk.Entry(frame_entrada)
entry_tiempo.grid(row=3, column=1)

# Botón para calcular la fuerza
boton_calcular_fuerza = tk.Button(ventana, text="Calcular Fuerza y Graficar", command=calcular_fuerza)
boton_calcular_fuerza.pack(pady=10)

# Resultados
frame_resultado = tk.Frame(ventana)
frame_resultado.pack(pady=10)

label_resultado_fuerza = tk.Label(frame_resultado, text="Fuerza ejercida: ")
label_resultado_fuerza.grid(row=0, column=0)

label_resultado_aceleracion = tk.Label(frame_resultado, text="Aceleración: ")
label_resultado_aceleracion.grid(row=1, column=0)

# Iniciar la ventana principal
ventana.mainloop()

