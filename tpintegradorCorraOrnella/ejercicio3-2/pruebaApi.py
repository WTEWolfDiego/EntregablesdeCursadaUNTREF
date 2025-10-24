import requests

BASE_URL = "https://pokeapi.co/api/v2/"

def verificar_pokeapi_datos():

    print("\n[CASO 1: berry/1]")
    try:
        url_berry1 = BASE_URL + "berry/1"
        response1 = requests.get(url_berry1)
        response1.raise_for_status() 
        data1 = response1.json()
        size_berry1 = data1.get("size")
        soil_dryness_berry1 = data1.get("soil_dryness")
        verif1_size = size_berry1 == 20
        verif1_soil = soil_dryness_berry1 == 15
        verif1_firmness = data1.get("firmness", {}).get("name") == "soft"
        print(f"  > Verificación Size (20): {'OK' if verif1_size else ' FALLO'}")
        print(f"  > Verificación Soil Dryness (15): {' OK' if verif1_soil else ' FALLO'}")
        print(f"  > Verificación Firmness ('soft'): {' OK' if verif1_firmness else 'FALLO'}")
    except requests.exceptions.RequestException as e:
        print(f" Error al conectar o recibir datos para berry/1: {e}")
        return 
    print("\n[CASO 2: berry/2]")
    try:
        url_berry2 = BASE_URL + "berry/2"
        response2 = requests.get(url_berry2)
        response2.raise_for_status()
        data2 = response2.json()
        size_berry2 = data2.get("size")
        soil_dryness_berry2 = data2.get("soil_dryness")
        verif2_firmness = data2.get("firmness", {}).get("name") == "super-hard"
        verif2_size_mayor = size_berry2 > size_berry1
        verif2_soil_igual = soil_dryness_berry2 == soil_dryness_berry1
        print(f"  > Verificación Firmness ('super-hard'): {' OK' if verif2_firmness else ' FALLO'}")
        print(f"  > Verificación Size (>{size_berry1}): {' OK' if verif2_size_mayor else ' FALLO'}")
        print(f"  > Verificación Soil Dryness (={soil_dryness_berry1}): {' OK' if verif2_soil_igual else ' FALLO'}")
    except requests.exceptions.RequestException as e:
        print(f" Error al conectar o recibir datos para berry/2: {e}")
    print("\n[CASO 3: pokemon/pikachu]")
    try:
        url_pikachu = BASE_URL + "pokemon/pikachu"
        response3 = requests.get(url_pikachu)
        response3.raise_for_status()
        data3 = response3.json()
        base_experience = data3.get("base_experience")
        tipos_nombres = [t["type"]["name"] for t in data3.get("types", [])]
        verif3_exp = 10 < base_experience < 1000
        verif3_tipo = "electric" in tipos_nombres
        print(f"  > Experiencia Base ({base_experience} > 10 y < 1000): {'OK' if verif3_exp else ' FALLO'}")
        print(f"  > Tipo ('electric'): {' OK' if verif3_tipo else 'FALLO'}")
    except requests.exceptions.RequestException as e:
        print(f" Error al conectar o recibir datos para pokemon/pikachu: {e}")
if __name__ == "__main__":
    verificar_pokeapi_datos()