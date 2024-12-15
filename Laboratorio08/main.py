import numpy as np

def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    Método de Bisección para encontrar raíces de una función.

    Parámetros:
    f : función para la cual se quiere encontrar la raíz.
    a : extremo inferior del intervalo.
    b : extremo superior del intervalo.
    tol : tolerancia para la convergencia.
    max_iter : número máximo de iteraciones.

    Retorna:
    c : aproximación de la raíz.
    """
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("La función no cambia de signo en el intervalo [a, b].")
    print(f"Bisección: Buscando raíz en el intervalo [{a}, {b}]")
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        print(f"Iteración {i}: c = {c}, f(c) = {fc}")
        if abs(fc) < tol or (b - a) / 2 < tol:
            print(f"Convergencia alcanzada en {i} iteraciones.\n")
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    raise RuntimeError("Método de Bisección no converge dentro del número máximo de iteraciones.")

def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    """
    Método de Newton-Raphson para encontrar raíces de una función.

    Parámetros:
    f : función para la cual se quiere encontrar la raíz.
    f_prime : derivada de la función f.
    x0 : estimación inicial.
    tol : tolerancia para la convergencia.
    max_iter : número máximo de iteraciones.

    Retorna:
    x : aproximación de la raíz.
    """
    print(f"Newton-Raphson: Iniciando con x0 = {x0}")
    x = x0
    for i in range(1, max_iter + 1):
        fx = f(x)
        fpx = f_prime(x)
        if fpx == 0:
            raise ZeroDivisionError("La derivada es cero. No se puede continuar.")
        x_new = x - fx / fpx
        print(f"Iteración {i}: x = {x_new}, f(x) = {f(x_new)}")
        if abs(f(x_new)) < tol:
            print(f"Convergencia alcanzada en {i} iteraciones.\n")
            return x_new
        x = x_new
    raise RuntimeError("Método de Newton-Raphson no converge dentro del número máximo de iteraciones.")

def false_position(f, a, b, tol=1e-6, max_iter=100):
    """
    Método de Falsa Posición (Regula Falsi) para encontrar raíces de una función.

    Parámetros:
    f : función para la cual se quiere encontrar la raíz.
    a : extremo inferior del intervalo.
    b : extremo superior del intervalo.
    tol : tolerancia para la convergencia.
    max_iter : número máximo de iteraciones.

    Retorna:
    c : aproximación de la raíz.
    """
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("La función no cambia de signo en el intervalo [a, b].")
    print(f"Falsa Posición: Buscando raíz en el intervalo [{a}, {b}]")
    for i in range(1, max_iter + 1):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        print(f"Iteración {i}: c = {c}, f(c) = {fc}")
        if abs(fc) < tol:
            print(f"Convergencia alcanzada en {i} iteraciones.\n")
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    raise RuntimeError("Método de Falsa Posición no converge dentro del número máximo de iteraciones.")

def secant(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Método de la Secante para encontrar raíces de una función.

    Parámetros:
    f : función para la cual se quiere encontrar la raíz.
    x0 : primera estimación inicial.
    x1 : segunda estimación inicial.
    tol : tolerancia para la convergencia.
    max_iter : número máximo de iteraciones.

    Retorna:
    x2 : aproximación de la raíz.
    """
    print(f"Secante: Iniciando con x0 = {x0}, x1 = {x1}")
    for i in range(1, max_iter + 1):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            raise ZeroDivisionError("División por cero en el método de la Secante.")
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        fx2 = f(x2)
        print(f"Iteración {i}: x2 = {x2}, f(x2) = {fx2}")
        if abs(fx2) < tol:
            print(f"Convergencia alcanzada en {i} iteraciones.\n")
            return x2
        x0, x1 = x1, x2
    raise RuntimeError("Método de la Secante no converge dentro del número máximo de iteraciones.")

# 1. y = ln(x − 2)
def f1(x):
    return np.log(x - 2)

def f1_derivative(x):
    return 1 / (x - 2)

# 2. y = e^(-x)
def f2(x):
    return np.exp(-x)

def f2_derivative(x):
    return -np.exp(-x)

# 3. y = e^x − x
def f3(x):
    return np.exp(x) - x

def f3_derivative(x):
    return np.exp(x) - 1

# 4. y = 10 * e^(x/2) * cos(2x)
def f4(x):
    return 10 * np.exp(x / 2) * np.cos(2 * x)

def f4_derivative(x):
    return 10 * np.exp(x / 2) * (0.5 * np.cos(2 * x) - 2 * np.sin(2 * x))

# 5. y = x^2 − 2
def f5(x):
    return x**2 - 2

def f5_derivative(x):
    return 2 * x

# 6. y = (x - 2)^(1/2) (usando potencias)
def f6(x):
    return np.sqrt(x - 2)

def f6_derivative(x):
    return 0.5 * (x - 2)**(-0.5)

# 7. y = x * cos(y) + y * sin(x)
def f7(y, x):
    return y - x * np.cos(y) - y * np.sin(x)

def f7_derivative(y, x):
    return 1 + x * np.sin(y) - np.sin(x)

# 8. y = 2 / x
def f8(x):
    return 2 / x

def f8_derivative(x):
    return -2 / x**2

def main():
    print("Resolución de Ecuaciones No Lineales con Métodos Numéricos\n")
    
    # 1. y = ln(x − 2)
    print("1. y = ln(x − 2)")
    try:
        # Método de Bisección
        a, b = 2.1, 4  # Intervalo que contiene la raíz x=3
        raiz_f1 = bisection(f1, a, b)
        print(f"La raíz de f1 es aproximadamente: {raiz_f1}\n")
    except Exception as e:
        print(f"No se pudo resolver f1: {e}\n")
    
    # 2. y = e^(-x)
    print("2. y = e^(-x)")
    try:
        # No tiene raíces reales, ya que e^(-x) > 0 para todo x
        print("La función f2 = e^(-x) no tiene raíces reales.\n")
    except Exception as e:
        print(f"No se pudo resolver f2: {e}\n")
    
    # 3. y = e^x − x
    print("3. y = e^x − x")
    try:
        # Verificamos si hay cambio de signo en algún intervalo
        # Evaluamos la función en varios puntos
        # f3(-1) = e^(-1) - (-1) ≈ 0.3679 +1 = 1.3679 >0
        # f3(0) =1 -0 =1 >0
        # f3(1) = e -1 ≈1.718 -1 =0.718 >0
        # f3(-2) = e^(-2) - (-2) ≈0.1353 +2 =2.1353 >0
        # Parece que f3(x) >0 para todo x, por lo tanto, no tiene raíces reales.
        print("La función f3 = e^x − x no tiene raíces reales.\n")
    except Exception as e:
        print(f"No se pudo resolver f3: {e}\n")
    
    # 4. y = 10 * e^(x/2) * cos(2x)
    print("4. y = 10 * e^(x/2) * cos(2x)")
    try:
        # Método de Falsa Posición
        # Buscamos el primer cero positivo cerca de pi/4 ≈0.7854
        a, b = 0.5, 1.0
        raiz_f4 = false_position(f4, a, b)
        print(f"La raíz de f4 cerca de π/4 es aproximadamente: {raiz_f4}\n")
    except Exception as e:
        print(f"No se pudo resolver f4: {e}\n")
    
    # 5. y = x^2 − 2
    print("5. y = x^2 − 2")
    try:
        # Método de Newton-Raphson para la raíz positiva
        x0 = 1.5
        raiz_f5 = newton_raphson(f5, f5_derivative, x0)
        print(f"La raíz positiva de f5 es aproximadamente: {raiz_f5}\n")
    except Exception as e:
        print(f"No se pudo resolver f5: {e}\n")
    
    # 6. y = sqrt(x - 2)
    print("6. y = sqrt(x - 2)")
    try:
        # Método de Falsa Posición
        # La raíz es x=2. Seleccionamos un intervalo [1.5, 2.5]
        # Sin embargo, f6(x) = sqrt(x-2) ≥0 y f6(2)=0
        # Para aplicar un método de raíz, reescribimos f6(x) = sqrt(x-2) -0 =0
        # Esto implica buscar x=2
        # Usaremos Bisección para demostrar
        a, b = 2, 3  # Intervalo que contiene la raíz x=2
        raiz_f6 = bisection(lambda x: f6(x), a, b)
        print(f"La raíz de f6 es aproximadamente: {raiz_f6}\n")
    except Exception as e:
        print(f"No se pudo resolver f6: {e}\n")
    
    # 7. y = x * cos(y) + y * sin(x)
    print("7. y = x * cos(y) + y * sin(x)")
    try:
        # Método de Newton-Raphson para resolver para y dado un x específico
        # Por ejemplo, x = 1.0
        x_val = 1.0
        print(f"Resolviendo para y en f7 con x = {x_val}")
        
        # Definimos la función de f7 para un x dado
        def func_f7(y):
            return f7(y, x_val)
        
        # Definimos la derivada de f7 para un x dado
        def func_f7_derivative(y):
            return f7_derivative(y, x_val)
        
        # Estimación inicial para y
        y0 = 0.5
        raiz_f7 = newton_raphson(func_f7, func_f7_derivative, y0)
        print(f"Para x={x_val}, la raíz de f7 es y≈{raiz_f7}\n")
    except Exception as e:
        print(f"No se pudo resolver f7: {e}\n")
    
    # 8. y = 2 / x
    print("8. y = 2 / x")
    try:
        # No tiene raíces reales, ya que 2/x !=0 para ningún x finito
        print("La función f8 = 2/x no tiene raíces reales.\n")
    except Exception as e:
        print(f"No se pudo resolver f8: {e}\n")

if __name__ == "__main__":
    main()
