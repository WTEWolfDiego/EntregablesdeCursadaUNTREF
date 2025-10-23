import math
#2 Escribir una función que, dado el ingreso de 3 variables (a, b, c),
#  retorne las raíces resultantes de una ecuación cuadrática

#Para usar raíz cuadrada
#Funcion que luego sera utilizada
def raicesCuadraticas(a,b,c):

    discriminante = b**2 - 4*a*c

    if discriminante < 0: #Si el discriminante es menor a cero, no hay raices reales
        print("No tiene solucion") 
    elif discriminante == 0: # Si el discriminante es igual a 0 hay una sola raiz real
        raiz = -b/(2*a)
        print("Tiene una sola raiz",raiz)
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print ("Tiene dos raices o soluciones ", x1, "y", x2) # Si el discriminante es mayor a 0, hay dos raices distintas

#Se solicita al usuario que ingrese el numero
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

raicesCuadraticas(a,b,c)
