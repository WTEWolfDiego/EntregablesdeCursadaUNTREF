
import requests
import time
import json 


# =========================================================================
# CONFIGURACIÓN BÁSICA
# =========================================================================
BASE_URL = "https://pokeapi.co/api/v2/"
ENDPOINT_BERRY_1 = "berry/1"

# Variables globales para compartir datos con el Caso 2
size_caso1 = None
dryness_caso1 = None


# =========================================================================
# CASO 1: berry/1
# =========================================================================

def test_caso1_berry1():
    """
    Caso 1: Verificar propiedades de berry1 (size, soil_dryness, firmness).
    """
    global size_caso1
    global dryness_caso1
    
    print("\n--- Ejecutar Caso 1: berry/1 ---")

    # Hacer un get a berry/1
    url = f"{BASE_URL}{ENDPOINT_BERRY_1}"
    print(f"Hacer GET a: {url}")
    
    # Usar requests.get()
    respuesta = requests.get(url)
    
    # Validar status code
    assert respuesta.status_code == 200, f"Error: Status code no es 200. Recibido: {respuesta.status_code}"
    
    # Obtener el JSON de la respuesta
    data = respuesta.json()
    
    # Almacenar datos para el Caso 2
    size_caso1 = data.get('size')
    dryness_caso1 = data.get('soil_dryness')

    # --- INICIO DE VERIFICACIONES ---

    # Verificar que el size sea 20
    assert data.get('size') == 20, f"Error de Size: Valor esperado 20. Recibido: {data.get('size')}"
    
    # Verificar que el soil_dryness sea 15
    assert data.get('soil_dryness') == 15, f"Error de Soil Dryness: Valor esperado 15. Recibido: {data.get('soil_dryness')}"
    
    # Verificar que en firmness, el name sea soft
    assert data.get('firmness').get('name') == "soft", f"Error de Firmness Name: Valor esperado 'soft'. Recibido: {data.get('firmness').get('name')}"

    print("GET y verificaciones del Caso 1 exitosas.")
    


# =========================================================================
# CASO 2: berry/2
# =========================================================================

def test_caso2_berry2():
    """
    Caso 2: Verificar propiedades de berry2 y comparar con Caso 1.
    """
    print("\n--- Ejecutar Caso 2: berry/2 ---")
    
    # Hacer un get a berry/2
    url = f"{BASE_URL}berry/2"
    print(f"Hacer GET a: {url}")
    
    respuesta = requests.get(url)
    
    # Validar status code
    assert respuesta.status_code == 200, f"Error: Status code no es 200. Recibido: {respuesta.status_code}"
    
    data = respuesta.json()
    
    # --- INICIO DE VERIFICACIONES ---
    
    # Verificar que en firmness, el name sea super-hard
    assert data.get('firmness').get('name') == "super-hard", f"Error de Firmness Name: Valor esperado 'super-hard'. Recibido: {data.get('firmness').get('name')}"
    
    # Verificar que el size sea mayor al del punto anterior (Caso 1)
    # Comparar valores esperados
    assert data.get('size') > size_caso1, f"Error de Size: Valor {data.get('size')} no es mayor que el del Caso 1 ({size_caso1})"
    
    # Verificar que el soil_dryness sea igual al del punto anterior (Caso 1)
    # Comparar valores esperados
    assert data.get('soil_dryness') == dryness_caso1, f"Error de Soil Dryness: Valor {data.get('soil_dryness')} no es igual que el del Caso 1 ({dryness_caso1})"

    print("GET y verificaciones del Caso 2 exitosas.")
    
    

# =========================================================================
# CASO 3: pokemon/pikachu
# =========================================================================

def test_caso3_pikachu():
    """
    Caso 3: Verificar experiencia base y tipo de Pikachu.
    """
    print("\n--- Ejecutar Caso 3: pokemon/pikachu ---")
    
    # Hacer un get a pokemon/pikachu
    url = f"{BASE_URL}pokemon/pikachu"
    print(f"Hacer GET a: {url}")
    
    respuesta = requests.get(url)
    
    # Validar status code
    assert respuesta.status_code == 200, f"Error: Status code no es 200. Recibido: {respuesta.status_code}"
    
    data = respuesta.json()
    
    # --- INICIO DE VERIFICACIONES ---
    
    base_experience = data.get('base_experience')

    # Verificar que su experiencia base es mayor a 10 y menor a 1000
    # Usar operadores relacionales y encadenar asserts.
    assert base_experience > 10, f"Error de Experiencia Base: {base_experience} no es mayor a 10."
    assert base_experience < 1000, f"Error de Experiencia Base: {base_experience} no es menor a 1000."
    
    # Verificar que su tipo es "electric"
    # El campo 'types' es una lista, se verifica el primer elemento
    primer_tipo = data.get('types')[0].get('type').get('name')
    assert primer_tipo == "electric", f"Error de Tipo: Valor esperado 'electric'. Recibido: {primer_tipo}"
    
    print("GET y verificaciones del Caso 3 exitosas.")

