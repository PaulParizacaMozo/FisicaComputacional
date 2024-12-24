
# GSA.py

import numpy as np
import time
from scipy.stats import gamma
from KronD import KronD  # Importa la función KronD

def tsallis_rnd(qv, Tqv, dim):
    """
    Genera números aleatorios según la distribución de Tsallis.
    """
    n = (3 - qv) / (qv - 1)
    s = np.sqrt(2 * (qv - 1)) / (Tqv ** (1 / (3 - qv)))
    cov = (n * (qv - 1) / (Tqv ** (2 / (3 - qv)))) ** -1
    mu = 0
    sigma = np.sqrt(cov)
    X = np.random.normal(mu, sigma, dim)
    U = gamma.rvs(n / 2, scale=1)
    Y = s * np.sqrt(U)
    Z = X / Y
    return Z

def GSA(funcion_objetivo, x_inicial, limites_inferiores=None, limites_superiores=None, qv=2.7, qa=-5, Imax=400):
    """
    Algoritmo GSA (Generalized Simulated Annealing) para optimización.
    """
    inicio_tiempo = time.time()

    x_optimo = x_inicial
    f_optimo = funcion_objetivo(x_inicial)
    f_mejor = f_optimo
    dimensiones = x_inicial.shape
    k = 1.380649e-23

    if limites_inferiores is not None:
        limites_inferiores = np.array(limites_inferiores)
    if limites_superiores is not None:
        limites_superiores = np.array(limites_superiores)

    for t in range(1, Imax + 1):
        Tqvo = Imax
        if qv == 1.0:
            Tqv = Tqvo / np.log(1 + t)
        elif qv == 2.0:
            Tqv = Tqvo / (1 + t)
        else:
            Tqv = Tqvo * ((2 ** (qv - 1)) - 1) / (((1 + t) ** (qv - 1)) - 1)

        Tqa = Tqv / t

        for _ in range(Imax // 5):
            if limites_inferiores is not None and limites_superiores is not None:
                dx = tsallis_rnd(qv, Tqv, dimensiones) * (limites_superiores - limites_inferiores)
                x_nuevo = x_optimo + dx
                x_nuevo = np.clip(x_nuevo, limites_inferiores, limites_superiores)
            else:
                dx = tsallis_rnd(qv, Tqv, dimensiones)
                x_nuevo = x_optimo + dx

            f_nuevo = funcion_objetivo(x_nuevo)
            delta_f = f_nuevo - f_optimo

            if delta_f < 0:
                Pa = 1
            elif delta_f >= 0 and qa < 1 and (1 + (qa - 1) * delta_f / (k * Tqa)) > 0:
                Pa = 1 / ((1 + (qa - 1) * delta_f / (k * Tqa)) ** (1 / (qa - 1)))
            else:
                Pa = 0

            if delta_f < 0 or Pa > np.random.rand():
                x_optimo = x_nuevo
                f_optimo = f_nuevo

            if f_optimo < f_mejor:
                x_optimo = x_nuevo
                f_mejor = f_optimo

    tiempo_transcurrido = time.time() - inicio_tiempo
    return x_optimo, f_mejor, tiempo_transcurrido

