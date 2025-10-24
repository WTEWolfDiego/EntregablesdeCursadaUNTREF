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

# Caso 3 
# ● El usuario se loguea al sitio como usuario standard user  x
# ● Agregar un elemento al carrito 
# ● Ir al carrito 
# ● Remover el artículo 
# ● Verificar que el sitio no tiene artículos agregados 
# ● Ir a “Continue Shopping” 
# ● Agregar 2 elementos 
# ● Ir al carrito 
# ● Verificar que los elementos existan 
# ● Hacer el checkout 
# ● Finalizar la compra 
# ● Verificar que la compra fue realizada 

def test_caso_3_3():
    driver = webdriver.Chrome()
    time.sleep(1)
    driver.maximize_window()

    driver.get('https://www.saucedemo.com/')
    time.sleep(1)

    #Ingreso datos de usuario y contraseña.
    driver.find_element(By.ID, 'user-name').send_keys ("standard_user")
    time.sleep(1)
    driver.find_element(By.ID, 'password').send_keys ('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)

    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    time.sleep(2)

    driver.find_element(By.ID, 'remove-sauce-labs-bike-light').click()
    #Compruebo si el carrito queda vacio
    carrito_vacio = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(carrito_vacio) == 0, "El carrito no esta vacio."
    print("Carrito vacio")

    time.sleep(1)

    driver.find_element(By.ID, 'continue-shopping').click()

    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    time.sleep(1)

    driver.find_element(By.ID,'add-to-cart-sauce-labs-fleece-jacket').click()
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    time.sleep(2)
    #Compruebo la cantidad de productos en el carrito
    prod_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(prod_carrito) == 2, ("Se esperaban dos productos, pero se encontraron: " + str(prod_carrito))
    print("Se encontraron dos productos en el carrito")

    driver.find_element(By.ID,'checkout').click()
    time.sleep(1)

    driver.find_element(By.ID,'first-name').send_keys('Hernan')
    driver.find_element(By.ID,'last-name').send_keys('Pacheco')
    driver.find_element(By.ID,'postal-code').send_keys(2820)
    time.sleep(1)

    driver.find_element(By.ID,'continue').click()
    time.sleep(1)

    driver.find_element(By.ID,'finish').click()
    #Compruebo si el mensaje al finalizar la compra es el esperado
    mensaje_compra = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert mensaje_compra == "Thank you for your order!", "El mensaje final no es el esperado."
    print("Compra completada Correctamente")

    driver.quit()