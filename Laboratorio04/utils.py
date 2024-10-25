
import numpy as np
from scipy.integrate import quad

# Evaluar la función de fuerza
def evaluar_fuerza(fuerza_str, x):
    return eval(fuerza_str)

# Calcular la integral del trabajo
def calcular_integral(fuerza_str, x_inicial, x_final):
    funcion_fuerza = lambda x: evaluar_fuerza(fuerza_str, x)
    trabajo_integral, _ = quad(funcion_fuerza, x_inicial, x_final)
    return trabajo_integral, _

# Calcular el trabajo usando sumatoria
def calcular_sumatoria(fuerza_str, x_inicial, x_final, n_intervalos):
    dx = (x_final - x_inicial) / n_intervalos
    suma_trabajo = 0
    for i in range(n_intervalos):
        x = x_inicial + i * dx
        suma_trabajo += evaluar_fuerza(fuerza_str, x) * dx
    return suma_trabajo
