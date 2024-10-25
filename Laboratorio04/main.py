
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from utils import evaluar_fuerza, calcular_sumatoria, calcular_integral
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para manejar el cálculo y la visualización
def calcular_trabajo():
    try:
        # Obtener valores de la interfaz
        fuerza_str = entrada_fuerza.get()
        x_inicial = float(entrada_x_inicial.get())
        x_final = float(entrada_x_final.get())
        n_intervalos = int(entrada_n_intervalos.get())
        
        # Calcular la integral del trabajo
        trabajo_integral, _ = calcular_integral(fuerza_str, x_inicial, x_final)
        
        # Calcular el trabajo usando sumatoria
        trabajo_sumatoria = calcular_sumatoria(fuerza_str, x_inicial, x_final, n_intervalos)
        
        # Calcular desviación porcentual
        desviacion = abs((trabajo_sumatoria - trabajo_integral) / trabajo_integral) * 100
        
        # Mostrar resultados en la interfaz
        resultado_integral.set(f"Trabajo por integral: {trabajo_integral:.4f}")
        resultado_sumatoria.set(f"Trabajo por sumatoria: {trabajo_sumatoria:.4f}")
        resultado_desviacion.set(f"Desviación porcentual: {desviacion:.2f}%")
        
        # Actualizar los gráficos
        actualizar_grafico(fuerza_str, x_inicial, x_final, n_intervalos, trabajo_integral, trabajo_sumatoria)
    
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

# Función para actualizar los gráficos
def actualizar_grafico(fuerza_str, x_inicial, x_final, n_intervalos, trabajo_integral, trabajo_sumatoria):
    x_vals = np.linspace(x_inicial, x_final, 1000)
    y_vals = evaluar_fuerza(fuerza_str, x_vals)
    
    # Limpiar las figuras antes de volver a dibujar
    ax_integral.clear()
    ax_sumatoria.clear()

    # Gráfico de la integral con un área bajo la curva más destacada
    ax_integral.plot(x_vals, y_vals, label="Fuerza variable", color='blue', linewidth=2)
    ax_integral.fill_between(x_vals, 0, y_vals, color='green', alpha=0.6, label=f"Trabajo (Integral): {trabajo_integral:.4f}")
    ax_integral.set_title("Gráfico de la Integral", fontsize=14)
    ax_integral.set_xlabel("Distancia (m)", fontsize=12)
    ax_integral.set_ylabel("Fuerza (N)", fontsize=12)
    ax_integral.set_xlim([0, x_final])  # Comenzar el eje x desde 0
    ax_integral.set_ylim([0, max(y_vals)])  # Comenzar el eje y desde 0
    ax_integral.legend()

    # Gráfico de la sumatoria
    dx = (x_final - x_inicial) / n_intervalos
    x_sum_vals = np.linspace(x_inicial, x_final, n_intervalos, endpoint=False)  # Generar los puntos sin incluir el final
    y_sum_vals = evaluar_fuerza(fuerza_str, x_sum_vals)
    
    # Dibujar las barras de la sumatoria desplazadas hacia la izquierda para alinear con la esquina superior izquierda
    ax_sumatoria.bar(x_sum_vals, y_sum_vals, width=dx, alpha=0.7, color='orange', edgecolor='black', label=f"Trabajo (Sumatoria): {trabajo_sumatoria:.4f}", linewidth=1, align='edge')
    
    # Dibujar la línea de la función en el mismo gráfico
    ax_sumatoria.plot(x_vals, y_vals, label="Fuerza variable", color='blue', linewidth=2)
    
    ax_sumatoria.set_title("Gráfico de la Sumatoria", fontsize=14)
    ax_sumatoria.set_xlabel("Distancia (m)", fontsize=12)
    ax_sumatoria.set_ylabel("Fuerza (N)", fontsize=12)
    ax_sumatoria.set_xlim([0, x_final])  # Comenzar el eje x desde 0
    ax_sumatoria.set_ylim([0, max(y_vals)])  # Comenzar el eje y desde 0
    ax_sumatoria.legend()

    # Redibujar los gráficos en la interfaz
    canvas_integral.draw()
    canvas_sumatoria.draw()

# Función para agregar placeholders en los campos de entrada
def placeholder(event, entry, text):
    if entry.get() == text:
        entry.delete(0, tk.END)
        entry.config(fg='black')

def add_placeholder(entry, text):
    entry.insert(0, text)
    entry.config(fg='gray')
    entry.bind("<FocusIn>", lambda event: placeholder(event, entry, text))
    entry.bind("<FocusOut>", lambda event: reset_placeholder(event, entry, text))

def reset_placeholder(event, entry, text):
    if entry.get() == "":
        entry.insert(0, text)
        entry.config(fg='gray')

# Interfaz gráfica
root = tk.Tk()
root.title("Cálculo del trabajo con fuerza variable")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# Estilo de los widgets
label_font = ('Arial', 12)
entry_font = ('Arial', 12)
button_font = ('Arial', 12, 'bold')
result_font = ('Arial', 12, 'bold')

# Labels y entradas de datos
tk.Label(root, text="Función de fuerza (en función de x):", font=label_font, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
entrada_fuerza = tk.Entry(root, font=entry_font)
entrada_fuerza.grid(row=0, column=1, padx=10, pady=10)
add_placeholder(entrada_fuerza, "Ej. 2*x**2")

tk.Label(root, text="Distancia inicial (m):", font=label_font, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
entrada_x_inicial = tk.Entry(root, font=entry_font)
entrada_x_inicial.grid(row=1, column=1, padx=10, pady=10)
add_placeholder(entrada_x_inicial, "Ej. 0")

tk.Label(root, text="Distancia final (m):", font=label_font, bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10)
entrada_x_final = tk.Entry(root, font=entry_font)
entrada_x_final.grid(row=2, column=1, padx=10, pady=10)
add_placeholder(entrada_x_final, "Ej. 10")

tk.Label(root, text="Número de intervalos para la sumatoria:", font=label_font, bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10)
entrada_n_intervalos = tk.Entry(root, font=entry_font)
entrada_n_intervalos.grid(row=3, column=1, padx=10, pady=10)
add_placeholder(entrada_n_intervalos, "Ej. 50")

# Botón para calcular (color neutro)
boton_calcular = tk.Button(root, text="Calcular trabajo", font=button_font, bg="#1E90FF", fg="white", command=calcular_trabajo)  # Cambiado a azul claro
boton_calcular.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

# Labels para mostrar resultados
resultado_integral = tk.StringVar()
tk.Label(root, textvariable=resultado_integral, font=result_font, bg="#f0f0f0").grid(row=5, column=0, columnspan=2)

resultado_sumatoria = tk.StringVar()
tk.Label(root, textvariable=resultado_sumatoria, font=result_font, bg="#f0f0f0").grid(row=6, column=0, columnspan=2)

resultado_desviacion = tk.StringVar()
tk.Label(root, textvariable=resultado_desviacion, font=result_font, bg="#f0f0f0").grid(row=7, column=0, columnspan=2)

# Crear figuras de Matplotlib para los gráficos
fig_integral, ax_integral = plt.subplots(figsize=(5, 3))
fig_sumatoria, ax_sumatoria = plt.subplots(figsize=(5, 3))

# Inicializar los gráficos vacíos en la interfaz
canvas_integral = FigureCanvasTkAgg(fig_integral, master=root)
canvas_integral.get_tk_widget().grid(row=8, column=0, padx=10, pady=10)

canvas_sumatoria = FigureCanvasTkAgg(fig_sumatoria, master=root)
canvas_sumatoria.get_tk_widget().grid(row=8, column=1, padx=10, pady=10)

# Iniciar la interfaz
root.mainloop()
