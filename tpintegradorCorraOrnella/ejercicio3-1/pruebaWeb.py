import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
import time

@pytest.fixture
def setup_teardown():
    firefox_options = Options()
    driver = webdriver.Firefox(options=firefox_options) 
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def login_standard_user(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_caso1_ordenar_por_precio(setup_teardown):
    driver = setup_teardown
    #Login
    login_standard_user(driver)
    #Ordenar
    select_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(select_element)
    select.select_by_value("lohi") 
    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    actual_prices = []
    #Verificar Ordenamiento
    for element in price_elements:
        actual_prices.append(float(element.text.replace('$', '')))
    expected_prices = sorted(actual_prices)
    assert actual_prices == expected_prices, \
        " Falla: Los elementos no están ordenados de precio bajo a alto."
    print(" Caso 1 OK: Los elementos están ordenados por precio (low to high).")

def test_caso2_checkout_errores(setup_teardown):
    driver = setup_teardown
    #Login
    login_standard_user(driver)
    #Agregar al carrito
    add_buttons = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
    for button in add_buttons:
        button.click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 6, "No todos los elementos están en el carrito."
    #Cheackout
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Ornella")
    driver.find_element(By.ID, "continue").click()
    error_message1 = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert error_message1 == "Error: Last Name is required", \
        "Falla: El mensaje de error de 'Last Name' no es correcto."
    driver.find_element(By.ID, "last-name").send_keys("Correa")
    driver.find_element(By.ID, "continue").click()
    error_message2 = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert error_message2 == "Error: Postal Code is required", \
        "Falla: El mensaje de error de 'Postal Code' no es correcto." 
    print(" Caso 2 OK: Las verificaciones de errores en el checkout son correctas.")

def test_caso3_remover_y_finalizar_compra(setup_teardown):
    driver = setup_teardown
    #Login
    login_standard_user(driver)
    #Agrego al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_badge) == 0, "Falla: El carrito aún muestra artículos agregados."
    driver.find_element(By.ID, "continue-shopping").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 2, " Falla: No se encontraron los 2 artículos agregados."
    #Checkout
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Ornella")
    driver.find_element(By.ID, "last-name").send_keys("Correa")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    thank_you_header = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert thank_you_header == "Thank you for your order!", \
        " Falla: El mensaje de confirmación de compra no es correcto."
    print(" Caso 3 OK: Se removió el artículo y se finalizó la compra exitosamente.")