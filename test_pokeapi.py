import requests
import pytest


# Configuracion 


BASE_URL = "https://pokeapi.co/api/v2"



# Caso 1 
# ● Hacer un get a berry/1 
# ● Verifi car que el size sea 20 
# ● Verifi car que el soil_dryness sea 15 
# ● Verifi car que en fi rmness, el name sea soft.

def test_berry_1():
    #Verifica los datos de la berry/1"""
    response = requests.get(f"{BASE_URL}/berry/1")
    assert response.status_code == 200, "No se pudo obtener berry/1"

    data = response.json()

    # Validar valores específicos
    assert data["size"] == 20, f"El size esperado era 20, se obtuvo {data['size']}"
    assert data["soil_dryness"] == 15, f"El soil_dryness esperado era 15, se obtuvo {data['soil_dryness']}"
    assert data["firmness"]["name"] == "soft", f"El firmness.name esperado era 'soft', se obtuvo {data['firmness']['name']}"


# Caso 2 
# ● Hacer un get a berry/2 
# ● Verifi car que en fi rmness, el name sea super-hard 
# ● Verifi car que el size sea mayor al del punto anterior 
# ● Verifi car que el soil_dryness sea igual al del punto anterior

def test_berry_2():
    #Compara datos de berry/2 con los de berry/1
    berry1 = requests.get(f"{BASE_URL}/berry/1").json()
    berry2 = requests.get(f"{BASE_URL}/berry/2").json()

    # Validar firmness
    assert berry2["firmness"]["name"] == "super-hard", (
        f"El firmness.name esperado era 'super-hard', se obtuvo {berry2['firmness']['name']}"
    )

    # Comparar tamaños
    assert berry2["size"] > berry1["size"], (
        f"Se esperaba que berry/2 tuviera size mayor a berry/1 "
        f"({berry2['size']} <= {berry1['size']})"
    )

    # Comparar soil_dryness (deben ser iguales)
    assert berry2["soil_dryness"] == berry1["soil_dryness"], (
        f"Se esperaba que berry/2 tuviera igual soil_dryness que berry/1 "
        f"({berry2['soil_dryness']} != {berry1['soil_dryness']})"
    )


#Caso 3
# ● Hacer un get a pikachu (https://pokeapi.co/api/v2/pokemon/pikachu/) 
# ● Verifi car que su experiencia base es mayor a 10 y menor a 1000 
# ● Verifi car que su tipo es “electric”

def test_pikachu():
   #Verifica la información del Pokémon Pikachu
    response = requests.get(f"{BASE_URL}/pokemon/pikachu/")
    assert response.status_code == 200, "No se pudo obtener la información de Pikachu"

    data = response.json()

    # Validar experiencia base
    base_exp = data["base_experience"]
    assert 10 < base_exp < 1000, f"La experiencia base {base_exp} no está entre 10 y 1000"

    # Validar tipo principal
    tipos = [t["type"]["name"] for t in data["types"]]
    assert "electric" in tipos, f"Pikachu no tiene tipo 'electric'. Tipos encontrados: {tipos}"
