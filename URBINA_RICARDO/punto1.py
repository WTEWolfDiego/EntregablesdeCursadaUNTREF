# Función para ver si un número es primo

#DATOS
#  los numeros menores o iguales a 1 no son primos
# el 2 sí es primo

def es_primo(x):
    if x <= 1:
        return False
    if x == 2:
        return True  
    # prueba desde el 2 hasta uno antes del número
    for i in range(2, x):
        if x % i == 0:
            return False
    return True  
# si lo puedo dividir, no es primo
# # si no lo pude dividir por ningun numero, es primo


# ingreso el número.
x = int(input("Probemos si este número es primo: "))

# muestra el resultado
if es_primo(x):
    print(f"{x} sí es un numero primo")
else:
    print(f"{x} no es un numero primo")
