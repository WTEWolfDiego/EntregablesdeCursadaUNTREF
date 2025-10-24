
import requests
def test_berry_api():
    url = "https://pokeapi.co/api/v2/berry/1"
    response = requests.get(url)

# Verificacion que la respuesta haya sido exitosa (código 200)
    assert response.status_code == 200, f"Falló la request, status: {response.status_code}"

# Si todo esta bien, convertimos la respuesta en JSON para poder leer los datos
    data = response.json()

# Se muestran los datos que nos interesan 
    print("Size:", data["size"])               
    print("Soil Dryness:", data["soil_dryness"])  
    print("Firmness Name:", data["firmness"]["name"]) 

# validacion de lo que pide la consigna
    assert data["size"] == 20
    assert data["soil_dryness"] == 15
    assert data["firmness"]["name"] == "soft"



