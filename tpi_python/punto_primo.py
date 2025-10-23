
# Definición de la función 
def es_primo(numero):
    """
    Retorna True si el número entero es primo, y False en caso contrario, 
    usando solo conceptos de bucles y condicionales.
    """
    
    # 1 y números menores no son primos
    if numero <= 1:
        return False
    
    # Verifico divisores desde 2 hasta (numero - 1)
    for i in range(2, numero):
        # Operador de módulo (%) y operador relacional (==)
        # Si el resto es 0, 'i' es un divisor
        if (numero % i) == 0:
            # Retorno de variables
            return False 
            
    # Si el ciclo termina, no se encontraron divisores, es primo
    return True

# ------------------
# Manejo de entrada
# ------------------

entrada_valida = False
entrada_usuario = "" # Variable para almacenar el texto que ingresa el usuario
numero_entero = 0    # Variable para almacenar el número convertido

# Se repite hasta que se ingrese un valor válido (o se asuma que es válido)
while not entrada_valida:
    
    # 1. Pido la entrada al usuario
    entrada_usuario = input("Por favor, ingrese un número entero: ")
    
    # 2. Convierto el texto a entero
    
    primer_caracter = entrada_usuario[0] # Tomo el primer elemento 

    if primer_caracter == '-' or ('0' <= primer_caracter <= '9'):
        entrada_valida = True
        numero_entero = int(entrada_usuario)
        
    else:
        print("Entrada no comienza con un dígito o signo negativo. Intente de nuevo.")


if es_primo(numero_entero):
    
    print(f"El número {numero_entero} Es primo")
    
else:
    print(f"El número {numero_entero} No es primo")