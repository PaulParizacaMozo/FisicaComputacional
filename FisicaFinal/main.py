
# main.py

import numpy as np
from RPS import RPS

def main():
    # Datos comunes
    Energia = np.array([100, 120, 140, 160, 180, 200])
    de = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    T = np.array([0.9, 0.85, 0.8, 0.75, 0.7, 0.65])
    um = 0.20

    # Ejecución para 80 kVp
    print("\n# Ejecución principal para 80 kVp")
    Eo_80 = 80
    dE_80 = 10
    Ef_80 = 80
    nom_archivo_ajuste_80 = 'ajuste_80kVp.png'
    nom_archivo_espectro_80 = 'espectro_80kVp.png'
    resultado_80 = RPS(Eo_80, dE_80, Ef_80, Energia, um, de, T, nom_archivo_ajuste_80, nom_archivo_espectro_80)
    print(f"Resultado para 80 kVp: Energía={resultado_80[0]}, Espectro={resultado_80[1]}, Error={resultado_80[2]:.2f}%")

    # Ejecución para 120 kVp
    print("\n# Ejecución principal para 120 kVp")
    Eo_120 = 120
    dE_120 = 10
    Ef_120 = 120
    nom_archivo_ajuste_120 = 'ajuste_120kVp.png'
    nom_archivo_espectro_120 = 'espectro_120kVp.png'
    resultado_120 = RPS(Eo_120, dE_120, Ef_120, Energia, um, de, T, nom_archivo_ajuste_120, nom_archivo_espectro_120)
    print(f"Resultado para 120 kVp: Energía={resultado_120[0]}, Espectro={resultado_120[1]}, Error={resultado_120[2]:.2f}%")

if __name__ == "__main__":
    main()

