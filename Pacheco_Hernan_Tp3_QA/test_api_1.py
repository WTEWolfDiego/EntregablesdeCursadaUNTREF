# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Contro de Calidad de Software
# Trabajo integrador Módulo 3 - APIs
# Alumno: Pacheco Hernan.

#Sitio: Poke Api (https://pokeapi.co/api/v2) 

import requests

# Caso 1 
# ● Hacer un get a berry/1 
# ● Verificar que el size sea 20 
# ● Verificar que el soil_dryness sea 15 
# ● Verificar que en firmness, el name sea soft. 

def test_berry1():
    url = "https://pokeapi.co/api/v2/berry/1"
    response = requests.get(url)
    data = response.json()
    
    # Comprobacion de datos solicitados
    assert data['size'] == 20, ("Se esperaba size 20, pero se obtuvo:" + str(data['size']))
    assert data['soil_dryness'] == 15, "Se esperaba que soil drynes sea de 15, pero se obtuvo: " + str(data['soil_dryness'])
    assert data['firmness']['name'] == 'soft', "Se esperaba que el firmnesss name fuera soft, pero se obtuvo: " + str(data['firmness']['name'])