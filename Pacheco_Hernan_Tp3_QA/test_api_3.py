# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Contro de Calidad de Software
# Trabajo integrador Módulo 3 - APIs
# Alumno: Pacheco Hernan.

#Sitio: Poke Api (https://pokeapi.co/api/v2) 

import requests

# Caso 3 
# ● Hacer un get a pikachu (https://pokeapi.co/api/v2/pokemon/pikachu/) 
# ● Verificar que su experiencia base es mayor a 10 y menor a 1000 
# ● Verificar que su tipo es “electric” 

def test_pikachu():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
    response = requests.get(url)
    data = response.json()
    
    # Comprobación de datos solicitados.
    # Experiencia
    assert 10 < data['base_experience'] < 1000, "Se esperaba que la experiencia base este entre 10 y 1000, pero la experiencia es: " + str(data['base_experience'])
    # Tipo
    tipos = [t['type']['name'] for t in data['types']]
    assert 'electric' in tipos, "Se esperaba tipo electrico, pero se encontro: " + tipos