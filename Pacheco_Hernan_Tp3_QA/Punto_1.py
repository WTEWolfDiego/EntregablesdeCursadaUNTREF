# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Contro de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 1
# Alumno: Pacheco Hernan.

# Punto 1: 
# Escribir un programa que dado el ingreso de un número retorne si el mismo es 
# primo o no. 

import math

es_primo = False
print('Ingresado un numero vamos a determinar si este es primo o no')

try: 
    numero = int(input('Ingrese el número a verificar: '))

    if numero <=1:
        print('Recorda que el numero debe ser positivo y mayor a 1')
    elif numero == 2:
        print ('El numero 2 no es primo')
    else:
        es_primo = True 

    for i in range (2,numero):
        if numero % i == 0:
            es_primo = False

    if es_primo == True:
        print ('El numero es primo.')

    else:
        print ('El numero no es primo.')        


except ValueError:
    print('El numero debe ser entero, y mayor a 1')
       
