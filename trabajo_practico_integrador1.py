# 1 Escribir un programa que dado el ingreso de un número retorne si el mismo es primo o no.


#Funcion que determina si el número ingresado por el usuario es primo o no
def esPrimo(numero):
    if numero <= 1: #Si un numero es menor o igual a 1 no es primo
        return False
    for i in range(2,numero): #Se recorre desde 2 hasta el numero
        if numero % i == 0:
            return False #Si encuentro algún número que divida al número exactamente (sin dejar resto), entonces NO es primo
    return True

#Se le solicita al usuario un numero
numero = int(input("Ingresa un número: "))

if esPrimo(numero):
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} no es primo")