import math

def es_primo():
  while True:
    opcion = input("Presioná 'q' para salir o cualquier otra tecla para continuar... ")
    if opcion.lower() == 'q':
      print("Saliendo...")
      break

    try:
      numero = int(input("Ingresa un número: "))
    except ValueError:
      print("Entrada inválida. Intenta de nuevo.")
      continue

    if numero < 2:
      print(f"❌ El {numero} no es primo")
      continue

    for divisor in range(2, int(math.sqrt(numero)) + 1):
      if numero % divisor == 0:
        print(f"❌ El {numero} no es primo")
        break
    else:
      print(f"✅ El {numero} es primo")

es_primo()