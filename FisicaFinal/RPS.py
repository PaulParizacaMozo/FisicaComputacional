
# RPS.py

import numpy as np
import time
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from GSA import GSA  # Importa la función GSA
from KronD import KronD  # Importa la función KronD

def RPS(Eo, dE, Ef, Energia, um, de, T, nom_archivo_ajuste, nom_archivo_espectro):
    """
    Función RPS para ajustar curvas de transmisión y espectros de energía.
    """
    inicio_tiempo = time.time()
    El = np.log10(Energia)
    if um > 0:
        uml = np.log10(um) * np.ones_like(Energia)
    else:
        raise ValueError("El coeficiente de atenuación 'um' debe ser positivo.")

    def polinomio_grado_5(x, a0, a1, a2, a3, a4, a5):
        return a0 + a1 * x + a2 * x**2 + a3 * x**3 + a4 * x**4 + a5 * x**5

    try:
        parametros_optimos, _ = curve_fit(polinomio_grado_5, El, uml, p0=[0, 0, 0, 0, 0, 0], maxfev=100000)
    except Exception as e:
        raise RuntimeError(f"Error al ajustar la curva: {e}")

    c = parametros_optimos
    um0 = 0.20 if Ef == 80 else 0.15
    Er = 10
    pe = 2
    contador = 0

    while Er > 1 or pe > 1:
        if contador > 120:
            break

        def funcion_objetivo(x):
            term1 = x[3] * ((x[0] * x[1]) / ((de + x[0]) * (de + x[1])))**x[2] * np.exp(-um0 * de)
            term2 = (1 - x[3]) * (
                0.2880 * np.exp(-0.2897 * de) +
                0.5000 * np.exp(-0.2807 * de) +
                0.1690 * np.exp(-0.2417 * de) +
                0.0430 * np.exp(-0.2342 * de)
            )
            return np.linalg.norm(T - (term1 + term2))**2

        x0 = np.random.rand(4)
        limites_inferiores = [0, 0, 0, 0]
        limites_superiores = [10, 0.99, 0.99, 0.99]
        res = GSA(funcion_objetivo, x0, limites_inferiores, limites_superiores, 2.7, -5, 200)
        x = res[0]

        d1 = np.arange(0, max(de), 0.001)
        T1 = (
            x[3] * ((x[0] * x[1]) / ((d1 + x[0]) * (d1 + x[1])))**x[2] * np.exp(-um0 * d1) +
            (1 - x[3]) * (
                0.2880 * np.exp(-0.2897 * d1) +
                0.5000 * np.exp(-0.2807 * d1) +
                0.1690 * np.exp(-0.2417 * d1) +
                0.0430 * np.exp(-0.2342 * d1)
            )
        )
        T1_interpolado = np.interp(d1, de, T)

        if Ef == 80:
            K0 = np.sum(396.2 * dE * T * np.exp(-um * 0))
            K2 = np.sum(396.2 * dE * T * np.exp(-um * 0.74))
            K1 = np.sum(396.2 * dE * T * np.exp(-um * 0.58))
            CSR = (0.58 * np.log(2 * K2 / K0) - 0.74 * np.log(2 * K1 / K0)) / np.log(K2 / K1)
            CSRct = np.sum(396.2 * dE * T1_interpolado * np.exp(-um * d1))
        elif Ef == 120:
            K0 = np.sum(629.2 * dE * T * np.exp(-um * 0))
            K2 = np.sum(629.2 * dE * T * np.exp(-um * 1.63))
            K1 = np.sum(629.2 * dE * T * np.exp(-um * 1.35))
            CSR = (1.35 * np.log(2 * K2 / K0) - 1.63 * np.log(2 * K1 / K0)) / np.log(K2 / K1)
            CSRct = np.sum(629.2 * dE * T1_interpolado * np.exp(-um * d1))

        T_interpolado = np.interp(d1, de, T)
        Er = np.abs(100 * (CSRct - CSR) / CSRct)
        pe = np.max(np.abs(T1_interpolado - T_interpolado))
        contador += 1

    # Graficar Curva de Transmisión
    plt.figure(figsize=(10, 7))
    plt.plot(de, T, 'o-', color='blue', label="Datos Experimentales")
    plt.plot(d1, T1, '-', color='red', label="Curva Ajustada")
    plt.title(f"Curva de Transmisión para {Ef} kVp")
    plt.xlabel('Espesor (g/cm²)')
    plt.ylabel('Curva de Transmisión')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(nom_archivo_ajuste, dpi=300)
    plt.show()

    # Graficar Espectro de Energía
    plt.figure(figsize=(10, 7))
    plt.plot(Energia, Energia, '-', color='green', label="Espectro de Energía")
    plt.title(f"Espectro de Energía para {Ef} kVp")
    plt.xlabel('Energía (kV)')
    plt.ylabel('Espectro de Energía')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(nom_archivo_espectro, dpi=300)
    plt.show()

    tiempo_transcurrido = time.time() - inicio_tiempo
    minutos, segundos = divmod(tiempo_transcurrido, 60)
    print(f"Tiempo total de cálculo para {Ef} kVp: {int(minutos)} min {segundos:.2f} s")

    return Energia, Energia, Er

