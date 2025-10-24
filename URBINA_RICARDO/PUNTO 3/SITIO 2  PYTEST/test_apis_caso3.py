import requests

#Validación de Pikachu y verificamos dos cosas: experiencia base y tipo "electric"

def test_pikachu_datos():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
    response = requests.get(url)
    assert response.status_code == 200, f"Falló la request, status: {response.status_code}"

    data = response.json()

# Validamos que la experiencia base esté entre 10 y 1000
    base_exp = data["base_experience"]
    print("Experiencia base:", base_exp, "| Exp_base esperada >10 y <1000 |")
    assert 10 < base_exp < 1000

# Validamos que el tipo incluya "electric"
    types = [t["type"]["name"] for t in data["types"]]
    print("Tipo:", types, "| Debe incluir 'electric' |")
    assert "electric" in types