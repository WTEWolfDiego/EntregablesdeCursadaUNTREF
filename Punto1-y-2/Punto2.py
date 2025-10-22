#Este código fue realizado por Jackson Rojas

import math

def raices_cuadraticas(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Dos raíces reales: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Una raíz real doble: x = {x}"
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        return f"Dos raíces complejas: x1 = {parte_real} + {parte_imaginaria}i, x2 = {parte_real} - {parte_imaginaria}i"

# Ejemplo de uso:
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

print(raices_cuadraticas(a, b, c))

