import math

def resolver_ecuacion_cuadratica(a, b, c):
    if a == 0:
        return "Error: 'a' no puede ser cero en una ecuación cuadrática."
    discriminante = b**2 - 4 * a * c
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return (x1, x2)
    elif discriminante == 0:
        x = -b / (2 * a)
        return (x, x)
    else:
        return "No hay soluciones reales (las raíces son números complejos)."
print("--- SOLUCIONADOR DE ECUACIONES CUADRÁTICAS (ax^2 + bx + c = 0) ---")
try:
    a = float(input("Ingrese el coeficiente 'a': "))
    b = float(input("Ingrese el coeficiente 'b': "))
    c = float(input("Ingrese el coeficiente 'c': "))
    resultado = resolver_ecuacion_cuadratica(a, b, c)
    print("\n--- RESULTADO ---")
    if isinstance(resultado, tuple):
        print(f"La ecuación {a}x^2 + {b}x + {c} = 0 tiene las siguientes raíces:")
        print(f"Raíz 1 (x1): {resultado[0]}")
        print(f"Raíz 2 (x2): {resultado[1]}")
    else:
        print(resultado)
except ValueError:
    print("\nError: Por favor, asegúrate de ingresar números válidos para a, b y c.")