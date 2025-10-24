import requests

# Constante
BASE_URL = "https://pokeapi.co/api/v2"

def test_get_berry_1():
    """Prueba: GET a berry/1 y verificar propiedades"""
    print("=== INICIANDO PRUEBA ===")
    print("Prueba: GET berry/1")

    # Hacer GET request
    url = f"{BASE_URL}/berry/1"
    response = requests.get(url)

    print(f"Status code: {response.status_code}")

    # Verificar que la peticion fue exitosa
    assert response.status_code == 200, "El status code debe ser 200"

    # Obtener el JSON
    data = response.json()

    # Verificar que el size sea 20
    assert data.get('size') == 20, f"El size debe ser 20, pero es {data.get('size')}"

    # Verificar que el soil_dryness sea 15
    assert data.get('soil_dryness') == 15, f"El soil_dryness debe ser 15, pero es {data.get('soil_dryness')}"

    # Verificar que en firmness, el name sea soft
    firmness = data.get('firmness', {})
    assert firmness.get('name') == 'soft', f"El firmness name debe ser 'soft', pero es '{firmness.get('name')}'"

    print("OK Prueba COMPLETADA exitosamente")

def test_get_berry_2():
    """Prueba: GET a berry/2 y comparar con berry/1"""
    print("=== INICIANDO PRUEBA ===")
    print("Prueba: GET berry/2")

    # Primero obtener datos de berry/1 para comparar
    url_berry_1 = f"{BASE_URL}/berry/1"
    response_berry_1 = requests.get(url_berry_1)
    data_berry_1 = response_berry_1.json()

    size_berry_1 = data_berry_1.get('size')
    soil_dryness_berry_1 = data_berry_1.get('soil_dryness')

    print(f"Berry 1 - Size: {size_berry_1}, Soil dryness: {soil_dryness_berry_1}")

    # Hacer GET request a berry/2
    url = f"{BASE_URL}/berry/2"
    response = requests.get(url)

    print(f"Status code: {response.status_code}")

    # Verificar que la peticion fue exitosa
    assert response.status_code == 200, "El status code debe ser 200"

    # Obtener el JSON
    data = response.json()

    # Verificar que en firmness, el name sea super-hard
    firmness = data.get('firmness', {})
    assert firmness.get('name') == 'super-hard', f"El firmness name debe ser 'super-hard', pero es '{firmness.get('name')}'"

    # Verificar que el size sea mayor al del punto anterior
    size_berry_2 = data.get('size')
    assert size_berry_2 > size_berry_1, f"El size de berry/2 ({size_berry_2}) debe ser mayor que el de berry/1 ({size_berry_1})"

    # Verificar que el soil_dryness sea igual al del punto anterior
    soil_dryness_berry_2 = data.get('soil_dryness')
    assert soil_dryness_berry_2 == soil_dryness_berry_1, f"El soil_dryness de berry/2 ({soil_dryness_berry_2}) debe ser igual al de berry/1 ({soil_dryness_berry_1})"

    print("OK Prueba COMPLETADA exitosamente")

def test_get_pikachu():
    """Prueba: GET a pokemon/pikachu y verificar propiedades"""
    print("=== INICIANDO PRUEBA ===")
    print("Prueba: GET pokemon/pikachu")

    # Hacer GET request a pikachu
    url = f"{BASE_URL}/pokemon/pikachu"
    response = requests.get(url)

    print(f"Status code: {response.status_code}")

    # Verificar que la peticion fue exitosa
    assert response.status_code == 200, "El status code debe ser 200"

    # Obtener el JSON
    data = response.json()

    # Verificar que su experiencia base es mayor a 10 y menor a 1000
    base_experience = data.get('base_experience')
    assert base_experience > 10, f"La base experience ({base_experience}) debe ser mayor a 10"
    assert base_experience < 1000, f"La base experience ({base_experience}) debe ser menor a 1000"

    # Verificar que su tipo es "electric"
    types = data.get('types', [])
    type_names = [t['type']['name'] for t in types]
    assert 'electric' in type_names, f"El tipo 'electric' debe estar en los tipos del pokemon, pero se encontraron: {type_names}"

    print("OK Prueba COMPLETADA exitosamente")
