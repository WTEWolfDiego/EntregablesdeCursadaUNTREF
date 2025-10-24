def es_primo(numero):
 
    # Los números menores a 2 no son primos
    if numero < 2:
        return False
    
    # 2 es el único número primo par
    if numero == 2:
        return True
    
    # Si el número es par y mayor a 2, no es primo
    if numero % 2 == 0:
        return False
    
    # Recorremos los numeros desde 3 hasta la raiz cuadrada del numero escrito, solo con numeros impares y verificamos si el numero escrito es divisible por alguno de ellos.
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
    
    return True


try:
    # Solicitar al usuario que ingrese un número
    numero = int(input("Ingrese un número para verificar si es primo: "))
    
    # Verificar si el número es primo
    if es_primo(numero):
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")
        
#Si hay un error inesperado, se muestra el error        
except Exception as e:
    print(f"Error inesperado: {e}")



