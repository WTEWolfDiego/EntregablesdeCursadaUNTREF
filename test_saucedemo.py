import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time

#1) Sitio: https://www.saucedemo.com/
# Caso 1
# ● El usuario se loguea al sitio como usuario standard user
# ● Ordenar los elementos por “price (low to high)”
# ● Verificar que los elementos estén ordenados

# Fixture para inicializar y cerrar el navegador
@pytest.fixture
def driver():

    
    chrome_options=Options()
    
       
    chrome_options.add_experimental_option("prefs", {
    "profile.password_manager_leak_detection": False
  })
    
    driver = webdriver.Chrome(options=chrome_options) 
    yield driver
    driver.quit()

def test_orden_precios(driver):
    #Abrir el sitio sauce demo
    
    
    
    
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    #Login como standard user
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(5)

    #Ordenar productos por "Price(low to high)"
    elemento_seleccion = driver.find_element(By.XPATH,'//select[@class="product_sort_container"]')
    seleccion = Select(elemento_seleccion)
    seleccion.select_by_visible_text('Price (low to high)')
    time.sleep(5)

    #Obtener precios de los productos
    precios_elementos = driver.find_elements(By.CLASS_NAME,"inventory_item_price")
    precios = [float(p.text.replace("$", "")) for p in precios_elementos]

    #Verificar que esten ordenados
    assert precios == sorted(precios), "Los productos no estan ordenados correctamente"

    driver.quit()

#Caso 2

#● El usuario se loguea al sitio como usuario standard user
#● Incorporar al carrito todos los elementos
#● Ir al carrito
#● Verifi car que todos los elementos estén en el carrito
#● Ir al checkout
#● Ingresar nombre y clickear “Continue”
#● Verifi car que aparece el error “Error: Last Name is required”
#● Ingresar un apellido y clickear “Continue”
#● Verifi car que aparece el error “Error: Postal Code is required”

def test_checkout_errors(driver):
    #Abrir el sitio sauce demo
    
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    #Login como standard user
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
  

    #Agregar todos los productos al carrito
    boton_add = driver.find_elements(By.XPATH, '//button[contains(text(),"Add to cart")]')
    for boton in boton_add:
        boton.click()

    time.sleep(2)

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verificar que todos los elementos estén en el carrito
    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(productos_carrito) == len(boton_add), "No todos los productos fueron agregados al carrito"

    # Ir al checkout
    driver.find_element(By.ID, "checkout").click()

     # Esperar a que aparezca el campo first-name
    wait = WebDriverWait(driver, 10)
    first_name = wait.until(EC.presence_of_element_located((By.ID,"first-name")))
    first_name.send_keys("Ana Laura")

    #Hacer click en Continue sin llenar el last name
    driver.find_element(By.ID, "continue").click()


    # Verificar error "Last Name is required"
    # Esperar que aparezca el error de Last Name
    error_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container")))
    error_text = error_element.text
    assert "Last Name is required" in error_text, "No apareció el error por Last Name"

    # Ingresar apellido y clickear “Continue” (sin postal code)
    driver.find_element(By.ID, "last-name").send_keys("Mansilla")
    driver.find_element(By.ID, "continue").click()

    wait = WebDriverWait(driver, 10)

    # Esperar que aparezca el error de Postal Code
    error_element2 = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container")))
    error_text2 = error_element2.text
    assert "Postal Code is required" in error_text2, "No apareció el error por Postal Code"


    driver.quit()  

# Caso 3
# ● El usuario se loguea al sitio como usuario standard user
# ● Agregar un elemento al carrito
# ● Ir al carrito
# ● Remover el artículo
# ● Verifi car que el sitio no tiene artículos agregados
# ● Ir a “Continue Shopping”
# ● Agregar 2 elementos
# ● Ir al carrito
# ● Verifi car que los elementos existan
# ● Hacer el checkout
# ● Finalizar la compra
# ● Verifi car que la compra fue realizada
def test_compra(driver):
    #Abrir el sitio sauce demo
    
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    #Login como standard user
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

    #Agregar un elemento al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    #Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    #Remover el articulo elegido
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    #Verificar que no haya articulos
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0, "El carrito debería estar vacío"

    #Ir a Continue Shopping
    driver.find_element(By.ID, "continue-shopping").click()

    #Agregar dos elementos
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    #Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    #Verificar que los dos elementos existan
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 2, f"Se esperaban 2 artículos, hay {len(cart_items)}"

    #Checkout
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Ana Laura")
    driver.find_element(By.ID, "last-name").send_keys("Mansilla")
    driver.find_element(By.ID, "postal-code").send_keys("1234")
    driver.find_element(By.ID, "continue").click()

    #Finalizar compra
    driver.find_element(By.ID, "finish").click()

    #Verificar compra completada
    wait = WebDriverWait(driver,10)
    confirmation = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert "Thank you for your order!" in confirmation.text, "La compra no fue completada correctamente"

    driver.quit()






