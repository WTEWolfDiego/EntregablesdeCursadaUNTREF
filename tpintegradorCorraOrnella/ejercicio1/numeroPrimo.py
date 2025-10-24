def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True
try:
    numero_ingresado = int(input("Ingresa un número entero para verificar si es primo: "))
    
    if es_primo(numero_ingresado):
        print(f"El número {numero_ingresado} es un número primo.")
    else:
        print(f"El número {numero_ingresado} NO es un número primo.")
except ValueError:
    print("Error: Por favor, ingresa un número entero válido.")