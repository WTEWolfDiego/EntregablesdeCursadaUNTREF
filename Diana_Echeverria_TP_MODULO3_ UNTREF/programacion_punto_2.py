import math

# funcion para calcular raices
def calcular_raices(a, b, c):
    # calcular discriminante
    discriminante = b * b - 4 * a * c
    
    print("\n--- RESULTADOS ---")
    
    # si discriminante es negativo
    if discriminante < 0:
        print("No hay raices reales")
        print("El discriminante es negativo")
        return
    
    # si discriminante es cero
    if discriminante == 0:
        raiz = -b / (2 * a)
        print("Hay una raiz doble:")
        print("x =", raiz)
        return
    
    # si discriminante es positivo
    raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print("Las raices son:")
    print("x1 =", raiz1)
    print("x2 =", raiz2)

# programa principal
print("Calculadora de ecuaciones cuadraticas")
print("ax^2 + bx + c = 0")

# pedir valores
a = float(input("Ingresa a: "))
b = float(input("Ingresa b: "))
c = float(input("Ingresa c: "))

# mostrar ecuacion
print("\nTu ecuacion es:", a, "x^2 +", b, "x +", c, "= 0")

# calcular y mostrar resultado
calcular_raices(a, b, c)

print("\nFin del programa")
