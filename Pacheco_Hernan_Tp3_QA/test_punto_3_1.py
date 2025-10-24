# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Contro de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 3
# Alumno: Pacheco Hernan.

# # Punto 3: 
# Automatizar los siguientes casos de prueba. Luego de que sean automatizados, 
# deben ser subidos a un repositorio git, se debe generar el archivo y debe retornar 
# un reporte HTML con los resultados de la ejecución. 
# 1) Sitio: https://www.saucedemo.com/ 


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest
import time

# Caso 1 
# ● El usuario se loguea al sitio como usuario standard user 
# ● Ordenar los elementos por “price (low to high)”
# ● Verificar que los elementos estén ordenados 

def test_caso1_menor_a_mayor():

    driver = webdriver.Chrome()
    time.sleep(1)
    driver.maximize_window()

    driver.get('https://www.saucedemo.com/')
    time.sleep(2)

    #Ingreso datos de usuario y contraseña.
    driver.find_element(By.ID, 'user-name').send_keys ("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, 'password').send_keys ('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    time.sleep(2)
    #Ordeno los elementos de menor a mayor
    select = Select (driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value ('lohi')
    
    # Verifico orden de precios
    precio_menor = driver.find_element(By.CLASS_NAME, "active_option")
    assert precio_menor.text == "Price (low to high)"
    time.sleep(5) 

    driver.quit()