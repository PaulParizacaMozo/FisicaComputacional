
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio y los límites modulares
Ua, Ub = -5, 5  # Límites en el eje X
Uc, Ud = -5, 5  # Límites en el eje Y
Nx, Ny = 50, 50  # Número de puntos en el espacio
dx = (Ub - Ua) / (Nx - 1)
dy = (Ud - Uc) / (Ny - 1)
dt = 0.01  # Paso de tiempo
T_max = 10  # Tiempo total de simulación
r = dt / (dx**2)  # Parámetro r para estabilidad en la ecuación de calor

# Coordenadas del punto de inicio (fuente) de la condición inicial si es centrada
x_centro, y_centro = 0.0, 0.0  # Ajustable si deseas otro punto central

# Parámetro para definir la condición inicial (0 para uniforme en 0, 1 para centrada en un punto)
condicion_inicial_tipo = 1  # Cambia a 0 para una condición uniforme en 0

# Definir la condición inicial según el valor de condicion_inicial_tipo
def initial_condition(x, y, tipo):
    if tipo == 0:
        return np.zeros((Nx, Ny))  # Condición inicial uniforme en 0
    elif tipo == 1:
        # Distribución gaussiana centrada en (x_centro, y_centro)
        return np.exp(-((x - x_centro)**2 + (y - y_centro)**2))
    else:
        raise ValueError("Tipo de condición inicial no reconocido. Usa 0 o 1.")

# Crear malla centrada según los límites definidos
x = np.linspace(Ua, Ub, Nx)
y = np.linspace(Uc, Ud, Ny)
X, Y = np.meshgrid(x, y)
u = initial_condition(X, Y, condicion_inicial_tipo)

# Definir el esquema de diferencias finitas para la ecuación de calor
def solve_heat_equation(u, r, Nx, Ny, T_max, dt, times_to_capture):
    num_steps = int(T_max / dt)
    u_new = u.copy()
    captured_frames = []  # Lista para almacenar los estados en los tiempos deseados
    
    for n in range(num_steps):
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                u_new[i, j] = (1 - 2 * r) * u[i, j] + r * (u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1])

        u = u_new.copy()
        
        # Guardar la solución en tiempos específicos
        if n in times_to_capture:
            captured_frames.append((u.copy(), n * dt))
    
    return captured_frames

# Tiempos para capturar (en número de pasos)
times_to_capture = [0, int(0.25 * T_max / dt), int(0.5 * T_max / dt), int(T_max / dt) - 1]
frames = solve_heat_equation(u, r, Nx, Ny, T_max, dt, times_to_capture)

# Graficar la solución en cuatro momentos específicos
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Evolución de la Temperatura en 4 Tiempos Diferentes")

for ax, (frame, time) in zip(axes.flatten(), frames):
    contour = ax.contourf(X, Y, frame, levels=50, cmap="jet")  # Usamos cmap="jet" para diferenciar
    ax.set_title(f"t = {time:.2f} s")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    fig.colorbar(contour, ax=ax, orientation="vertical", label="Temperatura")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

