import math

def ecuacion_cuadratica():
    a = float(input("Ingresa el coeficiente \"a\": "))
    b = float(input("Ingresa el coeficiente \"b\": "))
    c = float(input("Ingresa el coeficiente \"c\": "))

    if a == 0:
        return "No es una ecuación cuadrática"
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"La única raíz real (doble) es: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Las soluciones reales son: x1 = {x1}, x2 = {x2}"

if __name__ == "__main__":
    print(ecuacion_cuadratica())