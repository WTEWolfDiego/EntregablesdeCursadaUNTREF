# Intento de resolver una ecuación cuadrática con raíces reales o complejas (si el discriminante es negativo)

import math

try:
    # el usuario ingresa los valores
    a = float(input("Ingresá el valor de a: "))
    b = float(input("Ingresá el valor de b: "))
    c = float(input("Ingresá el valor de c: "))

    # se calcula el discriminante
    discriminante = b**2 - 4*a*c

    # ahora se verifica qué tipo de raíces tiene
    if discriminante < 0:

        # si es negativo, las raíces son complejas
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        print(f"x1 = {parte_real} + {parte_imaginaria}i")  # raíz con +
        print(f"x2 = {parte_real} - {parte_imaginaria}i")  # raíz con -
    else:
        # si el discriminante es 0 o positivo, las raíces son reales
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)

except ZeroDivisionError:
    print("No se puede dividir por cero. Modifica el valor de 'a'.")
