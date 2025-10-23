
# Importo el módulo 'math' para usar la función de raíz cuadrada (sqrt)
import math

def calcular_raices_cuadratica(a, b, c):
    """
    Esto calcula y retorna las raíces de una ecuación cuadrática ax^2 + bx + c = 0
    
    Retorna un diccionario con: las raíces o un mensaje de error
    """
    
    # Operadores para calcular el Discriminante (Delta = b^2 - 4ac)
    discriminante = (b**2) - (4 * a * c)
    
    # Estructuras If-Elif-Else y Operadores relacionales
    
    # Caso 1: Dos raíces reales distintas (Discriminante > 0)
    if discriminante > 0:
        
        # Aplico la fórmula cuadrática: (-b +- sqrt(Delta)) / (2a)
        # Uso math.sqrt() para la raíz cuadrada
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        
        # Retorno de variables (Diccionario)
        return {
            "estado": "Dos raíces reales distintas",
            "x1": raiz1,
            "x2": raiz2
        }
        
    # Caso 2: Una raíz real doble (Discriminante = 0)
    elif discriminante == 0:
        
        # Fórmula simplificada: -b / 2a
        raiz = (-b) / (2 * a)
        
        # Retorno de variables (Diccionario)
        return {
            "estado": "Una raíz real doble",
            "x": raiz
        }
        
    # Caso 3: No hay raíces reales (Discriminante < 0)
    else: # discriminante < 0
        
        # Retorno de variables (Diccionario con mensaje de error)
        return {
            "estado": "No hay raíces reales",
            "mensaje": "El discriminante es negativo, lo que resulta en raíces complejas."
        }


# --- Ejemplo de Uso ---

# Variables de prueba (Ecuación: x^2 - 5x + 6 = 0, Raíces: x=3 y x=2)
a_val = 1
b_val = -5
c_val = 6 

print(f"Ecuación a resolver: {a_val}x^2 + {b_val}x + {c_val} = 0")

# Llamado a la función
resultado = calcular_raices_cuadratica(a_val, b_val, c_val)

print("\nResultado del cálculo:")
print(resultado)