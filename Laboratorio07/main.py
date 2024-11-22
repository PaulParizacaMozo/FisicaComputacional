import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Clase para manejar placeholders en los inputs
class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", color="grey", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self["fg"]
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._set_placeholder)
        self._set_placeholder()

    def _clear_placeholder(self, event=None):
        if self["fg"] == self.placeholder_color:
            self.delete(0, tk.END)
            self["fg"] = self.default_fg_color

    def _set_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self["fg"] = self.placeholder_color

# Función para realizar la integración Monte Carlo
def monte_carlo_integration(func, a, b, num_points):
    if b == float('inf'):
        transformed_func = lambda t: func(1 / t) / t**2
        a, b = 1e-5, 1
        func = transformed_func

    x_random = np.random.uniform(a, b, num_points)
    y_max = max(func(x) for x in np.linspace(a, b, 1000))
    y_random = np.random.uniform(0, y_max, num_points)

    under_curve = y_random <= func(x_random)
    over_curve = ~under_curve

    area_rectangle = (b - a) * y_max
    integral = (under_curve.sum() / num_points) * area_rectangle

    return integral, x_random, y_random, func, a, b, under_curve, over_curve, y_max

# Función para limpiar la interfaz
def clear():
    entry_function.delete(0, tk.END)
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_points.delete(0, tk.END)
    entry_function._set_placeholder()
    entry_a._set_placeholder()
    entry_b._set_placeholder()
    entry_points._set_placeholder()
    label_result.config(text="Resultado: ")
    for widget in frame_plot.winfo_children():
        widget.destroy()

# Función para calcular la integral
def calculate():
    try:
        func_str = entry_function.get()
        func = lambda x: eval(func_str)
        a = float(entry_a.get().replace("-inf", "-1e10"))
        b = float(entry_b.get().replace("inf", "1e10"))
        num_points = int(entry_points.get())

        result, x_random, y_random, func, a, b, under_curve, over_curve, y_max = monte_carlo_integration(func, a, b, num_points)

        label_result.config(text=f"Resultado: {result:.6f}")

        # Graficar dentro de la interfaz con seaborn
        for widget in frame_plot.winfo_children():
            widget.destroy()

        sns.set(style="whitegrid")
        figure = plt.Figure(figsize=(6, 4), dpi=100)
        ax = figure.add_subplot(111)

        x = np.linspace(a, b, 1000)
        y = func(x)

        # Curva de la función
        ax.plot(x, y, label="Función", color="blue", linewidth=2.5)

        # Puntos bajo la curva
        ax.scatter(x_random[under_curve], y_random[under_curve],
                   color="green", s=5, label="Puntos bajo la curva", alpha=0.6)

        # Puntos sobre la curva
        ax.scatter(x_random[over_curve], y_random[over_curve],
                   color="red", s=5, label="Puntos sobre la curva", alpha=0.6)

        ax.set_title("Integración Monte Carlo", fontsize=14)
        ax.set_xlabel("x", fontsize=12)
        ax.set_ylabel("f(x)", fontsize=12)
        ax.legend(fontsize=10)
        ax.grid(True, linestyle="--", alpha=0.7)

        canvas = FigureCanvasTkAgg(figure, frame_plot)
        canvas.get_tk_widget().pack()
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Error", f"Error en los cálculos: {str(e)}")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Integrales - Monte Carlo")
root.geometry("800x600")

# Inputs y etiquetas
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Función f(x):").grid(row=0, column=0, padx=5, pady=5)
entry_function = PlaceholderEntry(frame_inputs, placeholder="np.exp(x**2)", width=30)
entry_function.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Límite inferior a:").grid(row=1, column=0, padx=5, pady=5)
entry_a = PlaceholderEntry(frame_inputs, placeholder="0 o -inf", width=15)
entry_a.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Límite superior b:").grid(row=2, column=0, padx=5, pady=5)
entry_b = PlaceholderEntry(frame_inputs, placeholder="1 o inf", width=15)
entry_b.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Número de puntos aleatorios:").grid(row=3, column=0, padx=5, pady=5)
entry_points = PlaceholderEntry(frame_inputs, placeholder="10000", width=15)
entry_points.grid(row=3, column=1, padx=5, pady=5)

# Botones
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_calculate = tk.Button(frame_buttons, text="Calcular", command=calculate)
btn_calculate.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(frame_buttons, text="Limpiar", command=clear)
btn_clear.pack(side=tk.LEFT, padx=5)

# Resultado
label_result = tk.Label(root, text="Resultado: ", font=("Arial", 14))
label_result.pack(pady=10)

# Frame para la gráfica
frame_plot = tk.Frame(root)
frame_plot.pack(pady=10, fill=tk.BOTH, expand=True)

# Ejecutar la interfaz
root.mainloop()

