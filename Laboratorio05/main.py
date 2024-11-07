
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Constante de gravedad
GRAVITY = 9.81

# Función para calcular energía y mostrar gráfica
def calcular_energia():
    try:
        # Obtenemos los valores de entrada
        masa = float(entry_masa.get())
        velocidad_inicial = float(entry_velocidad.get())
        altura = float(entry_altura.get())
        
        # Determinamos si usamos la gravedad o la aceleración ingresada
        if var_gravedad.get():
            aceleracion = GRAVITY
        else:
            aceleracion = float(entry_aceleracion.get())

        # Calcular la energía mecánica total inicial como referencia
        EK_inicial = 0.5 * masa * velocidad_inicial**2  # Energía cinética inicial
        EP_inicial = masa * aceleracion * altura  # Energía potencial inicial
        Em_total = EK_inicial + EP_inicial  # Energía mecánica total (constante)

        # Aumentar la precisión de la simulación con un rango de tiempo mayor y más puntos
        time = np.linspace(0, 6, 500)  # tiempo de 0 a 6 segundos, con 500 puntos para mayor precisión
        EK_values = []
        EP_values = []
        Em_values = []

        for t in time:
            # Altura y velocidad ajustadas para garantizar que la altura llegue exactamente a cero
            h = max(0, altura - 0.5 * aceleracion * t**2)  # La altura no puede ser negativa
            v = velocidad_inicial + aceleracion * t  # Velocidad a cada instante

            # Ajustar la energía potencial cuando la altura es cero
            if h == 0:
                EP = 0
            else:
                EP = masa * aceleracion * h  # Energía potencial en función de la altura
            
            # Energías en cada instante
            EK = 0.5 * masa * v**2
            Em = max(Em_total, EK)  # Aseguramos que Em esté siempre sobre EK después del cruce

            EK_values.append(EK)
            EP_values.append(EP)
            Em_values.append(Em)

        # Crear una figura separada para las fórmulas con estilo LaTeX
        fig_formula = Figure(figsize=(5, 1), dpi=100)
        ax_formula = fig_formula.add_subplot(111)
        ax_formula.axis("off")
        
        # Renderizar las fórmulas usando LaTeX
        formula_text = (f"$E_m = E_K + E_P = {Em_total:.2f}\\,J$\n"
                        f"$E_K = \\frac{{1}}{{2}} \\times {masa:.1f} \\times {velocidad_inicial:.1f}^2 = {EK_inicial:.2f}\\,J$\n"
                        f"$E_P = {masa:.1f} \\times {aceleracion:.2f} \\times {altura:.1f} = {EP_inicial:.2f}\\,J$")
        ax_formula.text(0.5, 0.5, formula_text, ha="center", va="center", fontsize=12, color="black", transform=ax_formula.transAxes)

        # Mostrar las fórmulas en la ventana de Tkinter
        canvas_formula = FigureCanvasTkAgg(fig_formula, master=ventana)
        canvas_formula.draw()
        canvas_formula.get_tk_widget().grid(row=5, column=0, columnspan=3, pady=10)

        # Graficar los resultados de las energías
        fig, ax = plt.subplots(figsize=(8, 6))  # Tamaño mayor para mejor visibilidad
        ax.plot(time, EK_values, label="Energía Cinética (EK)", color='purple')
        ax.plot(time, EP_values, label="Energía Potencial (EP)", color='orange')
        ax.plot(time, Em_values, label="Energía Mecánica Total (Em)", color='brown', linestyle='--')
        ax.set_xlabel("Tiempo (s)", fontsize=12)
        ax.set_ylabel("Energía (J)", fontsize=12)
        ax.set_title("Conservación de la Energía Mecánica", fontsize=14)
        ax.legend(fontsize=10, loc="upper right")
        ax.set_xlim(0, 6)  # Ajustamos el eje X para mostrar el rango completo de tiempo
        ax.set_ylim(0, max(Em_values) * 1.2)  # Ajustamos el eje Y para mayor espacio superior
        ax.grid()

        # Ajustes adicionales para márgenes
        plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)
        
        # Mostrar la gráfica en la ventana
        canvas = FigureCanvasTkAgg(fig, master=ventana)
        canvas.draw()
        canvas.get_tk_widget().grid(row=6, column=0, columnspan=3, pady=10)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos")

# Función para activar/desactivar el campo de aceleración
def toggle_aceleracion():
    if var_gravedad.get():
        entry_aceleracion.config(state='disabled')
    else:
        entry_aceleracion.config(state='normal')

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Energía Mecánica")
ventana.geometry("700x800")
ventana.configure(bg="#f0f4f7")

# Estilo de los entry para placeholders
def on_enter(e, placeholder):
    if e.widget.get() == placeholder:
        e.widget.delete(0, 'end')
        e.widget.config(fg='black')

def on_leave(e, placeholder):
    if e.widget.get() == '':
        e.widget.insert(0, placeholder)
        e.widget.config(fg='grey')

# Crear los campos de entrada con placeholders
entry_masa = tk.Entry(ventana, fg='grey', font=("Arial", 12))
entry_masa.insert(0, "Ingrese la masa en kg")
entry_masa.bind("<FocusIn>", lambda e: on_enter(e, "Ingrese la masa en kg"))
entry_masa.bind("<FocusOut>", lambda e: on_leave(e, "Ingrese la masa en kg"))
entry_masa.grid(row=0, column=1, padx=5, pady=5)

entry_velocidad = tk.Entry(ventana, fg='grey', font=("Arial", 12))
entry_velocidad.insert(0, "Ingrese la velocidad inicial en m/s")
entry_velocidad.bind("<FocusIn>", lambda e: on_enter(e, "Ingrese la velocidad inicial en m/s"))
entry_velocidad.bind("<FocusOut>", lambda e: on_leave(e, "Ingrese la velocidad inicial en m/s"))
entry_velocidad.grid(row=1, column=1, padx=5, pady=5)

entry_altura = tk.Entry(ventana, fg='grey', font=("Arial", 12))
entry_altura.insert(0, "Ingrese la altura en m")
entry_altura.bind("<FocusIn>", lambda e: on_enter(e, "Ingrese la altura en m"))
entry_altura.bind("<FocusOut>", lambda e: on_leave(e, "Ingrese la altura en m"))
entry_altura.grid(row=2, column=1, padx=5, pady=5)

entry_aceleracion = tk.Entry(ventana, fg='grey', font=("Arial", 12))
entry_aceleracion.insert(0, "Ingrese la aceleración en m/s²")
entry_aceleracion.bind("<FocusIn>", lambda e: on_enter(e, "Ingrese la aceleración en m/s²"))
entry_aceleracion.bind("<FocusOut>", lambda e: on_leave(e, "Ingrese la aceleración en m/s²"))
entry_aceleracion.grid(row=3, column=1, padx=5, pady=5)

# Etiquetas
tk.Label(ventana, text="Masa (kg):", bg="#f0f4f7", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
tk.Label(ventana, text="Velocidad Inicial (m/s):", bg="#f0f4f7", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
tk.Label(ventana, text="Altura (m):", bg="#f0f4f7", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
tk.Label(ventana, text="Aceleración (m/s²):", bg="#f0f4f7", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5)

# Checkbox para usar la gravedad
var_gravedad = tk.BooleanVar()
checkbox_gravedad = tk.Checkbutton(
    ventana, text="Usar gravedad (9.81 m/s²)", variable=var_gravedad, command=toggle_aceleracion, bg="#f0f4f7", font=("Arial", 12)
)
checkbox_gravedad.grid(row=3, column=2, padx=5, pady=5)

# Botón para calcular
btn_calcular = tk.Button(ventana, text="Calcular", command=calcular_energia, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
btn_calcular.grid(row=4, column=1, padx=5, pady=10)

# Iniciar el estado del campo de aceleración según el checkbox
toggle_aceleracion()

ventana.mainloop()
