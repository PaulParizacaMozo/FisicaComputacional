
import numpy as np
import matplotlib.pyplot as plt

def automata_celular(regla, pasos, tamano, estado_inicial):
    estado = np.zeros((pasos, tamano), dtype=int)
    estado[0, estado_inicial] = 1  # Configuración inicial personalizada
    
    for t in range(1, pasos):
        for i in range(1, tamano - 1):
            vecindario = tuple(estado[t - 1, i - 1:i + 2])
            estado[t, i] = regla.get(vecindario, 0)
    
    return estado

# Definir reglas
regla = {
    (0, 0, 0): 0,
    (0, 0, 1): 1,
    (0, 1, 0): 1,
    (0, 1, 1): 1,
    (1, 0, 0): 1,
    (1, 0, 1): 0,
    (1, 1, 0): 0,
    (1, 1, 1): 0
}

# Parámetros generales
pasos = 80
tamano = 101
casos = {
    "Una celda central activa": [tamano // 2],
    "Dos celdas juntas": [tamano // 2, (tamano // 2) + 1],
    "Celdas alternantes": [tamano // 2 - 5, tamano // 2 - 3, tamano // 2 - 1, tamano // 2 + 1, tamano // 2 + 3],
    "Bloque continuo": list(range(tamano // 2 - 10, tamano // 2 + 10)),
    "Celda extrema activa": [0],
    "Celda en el borde derecho activa": [tamano - 1]
}

# Procesar cada caso
for nombre, estado_inicial in casos.items():
    resultado = automata_celular(regla, pasos, tamano, estado_inicial)

    # Celdas activas por generación
    activas_por_generacion = np.sum(resultado, axis=1)

    # Visualización principal
    plt.figure(figsize=(10, 10))
    plt.imshow(resultado, cmap="binary", interpolation="nearest")
    plt.title(f"Evolución del Autómata Celular ({nombre})")
    plt.xlabel("Celdas")
    plt.ylabel("Generaciones")
    plt.show()

    # Gráfico: Celdas activas por generación
    plt.figure(figsize=(8, 4))
    plt.plot(activas_por_generacion, label="Celdas activas")
    plt.xlabel("Generaciones")
    plt.ylabel("Número de celdas activas")
    plt.title(f"Celdas activas por generación ({nombre})")
    plt.legend()
    plt.show()

