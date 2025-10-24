# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Contro de Calidad de Software
# Trabajo integrador Módulo 3 - APIs
# Alumno: Pacheco Hernan.

#Sitio: Poke Api (https://pokeapi.co/api/v2) 

import requests

# Caso 2 
# ● Hacer un get a berry/2 
# ● Verificar que en firmness, el name sea super-hard 
# ● Verificar que el size sea mayor al del punto anterior 
# ● Verificar que el soil_dryness sea igual al del punto anterior 

def test_berry2():
       
    berry_1 = requests.get("https://pokeapi.co/api/v2/berry/1").json()
    
    url = "https://pokeapi.co/api/v2/berry/2"
    response = requests.get(url)
    data = response.json()
    
    # Comprobación de datos solicitados.
    assert data['firmness']['name'] == 'super-hard', "Se esperaba que firmness name fuera 'super-hard', pero se obtuvo: " + str(data['firmness']['name'])
    assert data['size'] > berry_1['size'], "Se esperaba que el size de berry 2 sea mayor a: " + str(berry_1['size']) + "Pero se obtuvo: " + str(data['size'])
    assert data['soil_dryness'] == berry_1['soil_dryness'], "Se esperaba que el soil dryness de berry 2 sea igual a:"  + str(berry_1['soil_dryness']) + "Pero se obtuvo: " + str(data['soil_dryness'])