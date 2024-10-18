import tkinter as tk
from tkinter import messagebox

# Función para calcular la Fuerza
def calcular_fuerza():
    try:
        masa = float(entry_masa.get())
        aceleracion = float(entry_aceleracion.get())
        fuerza = masa * aceleracion
        messagebox.showinfo("Resultado", f"La Fuerza es: {fuerza:.2f} N")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "La masa o aceleración no pueden ser 0.")

# Función para calcular la Masa
def calcular_masa():
    try:
        fuerza = float(entry_fuerza.get())
        aceleracion = float(entry_aceleracion.get())
        if aceleracion == 0:
            raise ZeroDivisionError("La aceleración no puede ser 0.")
        masa = fuerza / aceleracion
        messagebox.showinfo("Resultado", f"La Masa es: {masa:.2f} kg")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))

# Función para calcular la Aceleración
def calcular_aceleracion():
    try:
        fuerza = float(entry_fuerza.get())
        masa = float(entry_masa.get())
        if masa == 0:
            raise ZeroDivisionError("La masa no puede ser 0.")
        aceleracion = fuerza / masa
        messagebox.showinfo("Resultado", f"La Aceleración es: {aceleracion:.2f} m/s²")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))

# Función para mostrar el menú principal
def mostrar_menu():
    ocultar_todo()
    frame_menu.pack(pady=20)

# Función para mostrar los campos de acuerdo a la opción seleccionada
def mostrar_campos(opcion):
    ocultar_todo()  # Ocultar todo antes de mostrar los nuevos campos
    if opcion == "fuerza":
        label_masa.pack(pady=5)
        entry_masa.pack(pady=5)
        label_aceleracion.pack(pady=5)
        entry_aceleracion.pack(pady=5)
        boton_calcular.config(command=calcular_fuerza)
    elif opcion == "masa":
        label_fuerza.pack(pady=5)
        entry_fuerza.pack(pady=5)
        label_aceleracion.pack(pady=5)
        entry_aceleracion.pack(pady=5)
        boton_calcular.config(command=calcular_masa)
    elif opcion == "aceleracion":
        label_fuerza.pack(pady=5)
        entry_fuerza.pack(pady=5)
        label_masa.pack(pady=5)
        entry_masa.pack(pady=5)
        boton_calcular.config(command=calcular_aceleracion)
    
    boton_calcular.pack(pady=10)
    boton_menu.pack(pady=10)

# Función para ocultar todos los widgets
def ocultar_todo():
    frame_menu.pack_forget()
    label_fuerza.pack_forget()
    entry_fuerza.pack_forget()
    label_masa.pack_forget()
    entry_masa.pack_forget()
    label_aceleracion.pack_forget()
    entry_aceleracion.pack_forget()
    boton_calcular.pack_forget()
    boton_menu.pack_forget()

# Configurar la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de la Segunda Ley de Newton")

# Frame inicial con los botones de selección
frame_menu = tk.Frame(ventana)
frame_menu.pack(pady=20)

# Botones para elegir qué calcular
boton_fuerza = tk.Button(frame_menu, text="Calcular Fuerza", width=20, command=lambda: mostrar_campos("fuerza"))
boton_fuerza.pack(pady=5)

boton_masa = tk.Button(frame_menu, text="Calcular Masa", width=20, command=lambda: mostrar_campos("masa"))
boton_masa.pack(pady=5)

boton_aceleracion = tk.Button(frame_menu, text="Calcular Aceleración", width=20, command=lambda: mostrar_campos("aceleracion"))
boton_aceleracion.pack(pady=5)

# Campos de entrada (no visibles al inicio)
label_fuerza = tk.Label(ventana, text="Fuerza (N):")
entry_fuerza = tk.Entry(ventana)

label_masa = tk.Label(ventana, text="Masa (kg):")
entry_masa = tk.Entry(ventana)

label_aceleracion = tk.Label(ventana, text="Aceleración (m/s²):")
entry_aceleracion = tk.Entry(ventana)

# Botón para realizar el cálculo
boton_calcular = tk.Button(ventana, text="Calcular")

# Botón para regresar al menú
boton_menu = tk.Button(ventana, text="Volver al Menú", command=mostrar_menu)

# Iniciar el loop de la aplicación
ventana.mainloop()
