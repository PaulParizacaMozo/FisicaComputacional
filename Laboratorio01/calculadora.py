import tkinter as tk
from tkinter import messagebox

# Función para manejar los cálculos y mostrar resultados
def calcular(formula, variable_a_calcular, valores, ventana):
    try:
        if formula == 'a':  # ∆x = v × ∆t
            v = float(valores.get('v', 0))
            t = float(valores.get('t', 0))
            if variable_a_calcular == 'Distancia':
                resultado = v * t
            elif variable_a_calcular == 'Velocidad':
                resultado = float(valores['d']) / t
            elif variable_a_calcular == 'Tiempo':
                resultado = float(valores['d']) / v
            mostrar_resultado(ventana, f'Resultado: {resultado:.2f}')
        
        elif formula == 'b':  # ∆x = Vi∆t + (α∆t²)/2
            vi = float(valores.get('vi', 0))
            a = float(valores.get('a', 0))
            t = float(valores.get('t', 0))
            if variable_a_calcular == 'Distancia':
                resultado = vi * t + (a * (t**2)) / 2
            elif variable_a_calcular == 'Velocidad Inicial':
                resultado = (float(valores['d']) - (a * (t**2)) / 2) / t
            elif variable_a_calcular == 'Aceleración':
                resultado = 2 * (float(valores['d']) - vi * t) / (t**2)
            mostrar_resultado(ventana, f'Resultado: {resultado:.2f}')
        
        elif formula == 'c':  # Vf = Vi + α∆t
            vi = float(valores.get('vi', 0))
            a = float(valores.get('a', 0))
            t = float(valores.get('t', 0))
            if variable_a_calcular == 'Velocidad Final':
                resultado = vi + a * t
            elif variable_a_calcular == 'Velocidad Inicial':
                resultado = float(valores['vf']) - a * t
            elif variable_a_calcular == 'Aceleración':
                resultado = (float(valores['vf']) - vi) / t
            mostrar_resultado(ventana, f'Resultado: {resultado:.2f}')
    
    except ZeroDivisionError:
        mostrar_resultado(ventana, "Error: División por cero no permitida.")
    except ValueError:
        mostrar_resultado(ventana, "Error: Valor inválido, asegúrate de ingresar números.")

# Función para mostrar el resultado y botones finales
def mostrar_resultado(ventana, resultado):
    limpiar_ventana(ventana)
    
    tk.Label(ventana, text=resultado).pack(pady=10)
    
    tk.Button(ventana, text="Volver al inicio", command=lambda: ventana_principal(ventana)).pack()
    tk.Button(ventana, text="Cerrar", command=ventana.quit).pack()

# Función para seleccionar las variables y hacer el cálculo
def ventana_valores(ventana, formula, variable_a_calcular):
    limpiar_ventana(ventana)
    ventana.title(f"Calcular {variable_a_calcular}")
    
    campos = {}
    
    def calcular_resultado():
        valores = {key: entry.get() for key, entry in campos.items()}
        calcular(formula, variable_a_calcular, valores, ventana)
    
    # Campos de entrada según la fórmula y la variable
    if formula == 'a':
        if variable_a_calcular == 'Distancia':
            campos['v'] = tk.Entry(ventana)
            campos['t'] = tk.Entry(ventana)
        elif variable_a_calcular == 'Velocidad':
            campos['d'] = tk.Entry(ventana)
            campos['t'] = tk.Entry(ventana)
        elif variable_a_calcular == 'Tiempo':
            campos['d'] = tk.Entry(ventana)
            campos['v'] = tk.Entry(ventana)
    
    elif formula == 'b':
        if variable_a_calcular == 'Distancia':
            campos['vi'] = tk.Entry(ventana)
            campos['a'] = tk.Entry(ventana)
            campos['t'] = tk.Entry(ventana)
        elif variable_a_calcular == 'Velocidad Inicial':
            campos['d'] = tk.Entry(ventana)
            campos['a'] = tk.Entry(ventana)
            campos['t'] = tk.Entry(ventana)
        elif variable_a_calcular == 'Aceleración':
            campos['d'] = tk.Entry(ventana)
            campos['vi'] = tk.Entry(ventana)
            campos['t'] = tk.Entry(ventana)
    
    elif formula == 'c':
        if variable_a_calcular == 'Velocidad Final':
            campos['vi'] = tk.Entry(ventana)
            campos['a'] = tk.Entry(ventana)
            campos['t'] = tk.Entry(ventana)
        elif variable_a_calcular == 'Velocidad Inicial':
            campos['vf'] = tk.Entry(ventana)
            campos['a'] = tk.Entry(ventana)
            campos['t'] = tk.Entry(ventana)
        elif variable_a_calcular == 'Aceleración':
            campos['vf'] = tk.Entry(ventana)
            campos['vi'] = tk.Entry(ventana)
            campos['t'] = tk.Entry(ventana)
    
    # Colocando los campos en la ventana
    for idx, (key, entry) in enumerate(campos.items()):
        tk.Label(ventana, text=f"Ingresar {key}:").grid(row=idx, column=0, pady=5)
        entry.grid(row=idx, column=1, pady=5)
    
    tk.Button(ventana, text="Calcular", command=calcular_resultado).grid(row=len(campos), column=0, columnspan=2, pady=10)

# Ventana para seleccionar la variable a calcular
def ventana_seleccion(ventana, formula):
    limpiar_ventana(ventana)
    ventana.title("Selecciona lo que quieres calcular")
    
    opciones = {
        'a': ['Distancia', 'Velocidad', 'Tiempo'],
        'b': ['Distancia', 'Velocidad Inicial', 'Aceleración'],
        'c': ['Velocidad Final', 'Velocidad Inicial', 'Aceleración']
    }
    
    tk.Label(ventana, text="Selecciona la variable que deseas calcular:").pack(pady=10)
    
    for opcion in opciones[formula]:
        tk.Button(ventana, text=f"Calcular {opcion}", command=lambda op=opcion: ventana_valores(ventana, formula, op)).pack(pady=5)

# Ventana principal para seleccionar la fórmula
def ventana_principal(ventana):
    limpiar_ventana(ventana)
    ventana.title("Calculadora Física")
    
    tk.Label(ventana, text="Selecciona la fórmula que deseas utilizar").pack(pady=10)
    
    tk.Button(ventana, text="Fórmula a: ∆x = v × ∆t", command=lambda: ventana_seleccion(ventana, 'a')).pack(pady=5)
    tk.Button(ventana, text="Fórmula b: ∆x = Vi∆t + (α∆t²)/2", command=lambda: ventana_seleccion(ventana, 'b')).pack(pady=5)
    tk.Button(ventana, text="Fórmula c: Vf = Vi + α∆t", command=lambda: ventana_seleccion(ventana, 'c')).pack(pady=5)

# Función para limpiar la ventana antes de mostrar nuevos contenidos
def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana_principal(ventana)
ventana.mainloop()

