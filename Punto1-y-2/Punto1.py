#Este código fue realizado por Jackson Rojas

# Pedir al usuario un número
numero = int(input("Ingrese un número: "))

# Verificar si el número es primo
if numero < 2:
    print("No es un número primo.")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):  # Basta con revisar hasta la raíz cuadrada
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print("Es un número primo.")
    else:
        print("No es un número primo.")
