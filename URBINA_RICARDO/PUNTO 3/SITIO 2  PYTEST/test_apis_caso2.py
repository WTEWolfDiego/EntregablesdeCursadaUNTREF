# Caso 2 - Comparación entre berry/1 y berry/2
import requests

# Primero traemos los datos de berry/1
def test_berry_comparacion():
    
    ref = requests.get("https://pokeapi.co/api/v2/berry/1").json()
    ref_size = ref["size"]     
    ref_soil_dryness = ref["soil_dryness"]

# Ahora consultamos berry/2
    data = requests.get("https://pokeapi.co/api/v2/berry/2").json()

    # Verificamos que la irmness sea "super-hard"
    print(" Firmness:", data["firmness"]["name"], "| Esperado: super-hard |")
    assert data["firmness"]["name"] == "super-hard"

    # Verificamos que el size sea mayor al de berry/1
    print(" Size:", data["size"], "| Mayor que berry/1 (", ref_size, ") |")
    assert data["size"] > ref_size

    # Verificamos que el soil_dryness sea igual a la de berry/1
    print(" Soil Dryness:", data["soil_dryness"], "| Igual a berry/1 (", ref_soil_dryness, ") |")
    assert data["soil_dryness"] == ref_soil_dryness

