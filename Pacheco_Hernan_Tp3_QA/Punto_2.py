# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Contro de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 2
# Alumno: Pacheco Hernan.

# Punto 2: 
# Escribir una función que, dado el ingreso de 3 variables (a, b, c), retorne las raíces 
# resultantes de una ecuación cuadrática.

import math

print('Calculo de una ecuación cuadrática.')

#Solicitar el ingreso de 3 numeros al usuario.

a = float(input('Ingrese el primer valor a: '))
b = float(input('Ingrese el segundo valor b: '))
c = float(input('Ingrese el tercer valor c: '))

#Tomando los valores ingresados se calcula el discriminante

discriminante = b**2 - 4*a*c 

if discriminante > 0:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)

    print('Los dos posibles resultados con discriminante positivo son: ')
    print(x1)
    print(x2)

elif discriminante == 0:
    x = -b / (2 * a)
    print ('Si el discriminante es igual a 0 el resultado es: ')

else:
    print('El discriminante es negativo, por lo tanto no hay solución posible.')