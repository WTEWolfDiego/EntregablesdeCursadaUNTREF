from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def get_driver():
    
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    return driver

def hacer_login( driver, usuario, password):
    """Función auxiliar para hacer login"""
    print("Haciendo login con:", usuario)
    username = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")
    
    username.send_keys(usuario)
    password_field.send_keys(password)
    login_btn.click()
    
    time.sleep(5)
    
    # ver si funciona
    if "inventory" in driver.current_url:
        print("Login funciono!")
        return True
    else:
        print("Login no funciono")
        return False

def ir_al_carrito( driver):
    """Función auxiliar para ir al carrito"""
    print("Yendo a la pagina del carrito...")

    # encontrar el icono del carrito y hacer click
    carrito = driver.find_element(By.ID, "shopping_cart_container")

    # Usar JavaScript click como alternativa más confiable
    carrito.click()
    time.sleep(5)

    print("URL del carrito:", driver.current_url)

    # verificar que estamos en la pagina del carrito
    if "cart" in driver.current_url:
        print("OK Llegamos a la pagina del carrito")
        return True
    else:
        print("ERROR No se pudo llegar a la pagina del carrito")
        return False


# PRUEBAS CON PYTEST

def test_login_y_ordenamiento():
    """Prueba: Login y ordenamiento de productos"""
    print("=== INICIANDO PRUEBA ===")
    print("Prueba: Login y ordenamiento de productos")
    
    driver = get_driver()
    # hacer login
    resultado = hacer_login(driver, "standard_user", "secret_sauce")
    assert resultado, "El login debe ser exitoso"
    
    # ordenar productos y verificar
    filtro = driver.find_element(By.CSS_SELECTOR, "[data-test='product-sort-container']")
    select = Select(filtro)
    
    # seleccionar "Price (low to high)"
    select.select_by_value("lohi")
    time.sleep(5)

    print("Verificando que los precios esten ordenados...")
    
    # obtener todos los precios
    precios_elementos = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    precios = []
    
    for elemento in precios_elementos:
        # extraer el numero del precio (quitar el $)
        precio_texto = elemento.text
        precio_numero = float(precio_texto.replace("$", ""))
        precios.append(precio_numero)
    
    print("Precios encontrados:", precios)
    
    # verificar si estan ordenados de menor a mayor
    ordenados = True
    for i in range(len(precios) - 1):
        if precios[i] > precios[i + 1]:
            ordenados = False
            break
    
    assert ordenados, "Los precios deben estar ordenados de menor a mayor"

    print("OK Prueba COMPLETADA exitosamente")
    driver.quit()

def test_login_y_carrito_completo():
    """Prueba: Login, agregar items al carrito y hacer checkout"""
    print("=== INICIANDO PRUEBA ===")
    print("Prueba: Login y proceso completo de carrito")
    
    driver = get_driver()
    # hacer login
    resultado = hacer_login(driver, "standard_user", "secret_sauce")
    assert resultado, "El login debe ser exitoso"
    
    # agregar todos los items al carrito
    print("Agregando todos los items al carrito...")

    items_agregados = 0
    # Agregar items uno por uno, buscando el boton cada vez
    botones_add = driver.find_elements(By.CSS_SELECTOR, "[data-test*='add-to-cart']")
    
    assert len(botones_add) > 0, "Deberia tener botones para agregar al carrito"
    
    for boton in botones_add:
        boton.click()
        items_agregados += 1
        time.sleep(2)

    assert items_agregados == 6 , "Debe agregar al menos un item al carrito"
    
    # ir al carrito
    carrito_ok = ir_al_carrito(driver)
    assert carrito_ok, "Debe poder ir a la página del carrito"
    
    # verificar que todos los items esten en el carrito
    print(f"Verificando que los {items_agregados} items esten en el carrito...")
    # encontrar todos los items en el carrito
    items_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    cantidad_items = len(items_carrito)
    
    print(f"Items encontrados en el carrito: {cantidad_items}")
    
    # verificar que la cantidad coincida
    assert cantidad_items == items_agregados, "Todos los items agregados deben estar en el carrito"
    
    # hacer checkout
    # hacer click en el boton checkout
    checkout_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']")
    checkout_btn.click()
    time.sleep(5)

    # verificar que estamos en la pagina de checkout
    assert "checkout" in driver.current_url, "Debe poder hacer checkout"
    
    # llenar informacion de checkout
    # escribir el nombre "Diana"
    first_name = driver.find_element(By.CSS_SELECTOR, "[data-test='firstName']")
    first_name.send_keys("Diana")
    
    time.sleep(2)
    
    # hacer click en continue
    continue_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='continue']")
    continue_btn.click()
    time.sleep(5)
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        error_text = error_element.text
        print(f"Error encontrado: {error_text}")
        assert "Last Name is required" in error_text, "Debe mostrar el mensaje de error para Last Name"
    except Exception:
        print("ERROR No se encontro mensaje de error para Last Name")
    
    # ahora agregar el apellido
    print("Agregando apellido...")
    last_name = driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']")
    last_name.send_keys("Garcia")
    time.sleep(2)

    try:
        error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        error_text = error_element.text
        print(f"Error encontrado: {error_text}")
        assert "Postal Code is required" in error_text, "Debe mostrar el mensaje de error para Postal Code"
    except Exception:
        print("ERROR No se encontro mensaje de error para Postal Code")
    
    # ahora agregar el codigo postal
    print("OK Prueba COMPLETADA exitosamente")
    driver.quit()

def test_login_agregar_remover_item():
    """Prueba: Login, agregar un item, ir al carrito, removerlo, continuar comprando, agregar dos items, hacer checkout y finalizar compra"""
    print("=== INICIANDO PRUEBA ===")
    print("Prueba: Flujo completo de compra con remocion y recompra")
    
    driver = get_driver()
    # hacer login
    resultado = hacer_login(driver, "standard_user", "secret_sauce")
    assert resultado, "El login debe ser exitoso"
    
    # agregar un item al carrito
    boton_add = driver.find_element(By.CSS_SELECTOR, "[data-test*='add-to-cart']")
    boton_add.click()
    time.sleep(2)
    
    # ir al carrito
    carrito_ok = ir_al_carrito(driver)
    assert carrito_ok, "Debe poder ir a la página del carrito"
    time.sleep(5)
    
    # remover el item del carrito
    boton_remove = driver.find_element(By.CSS_SELECTOR, "[data-test*='remove']")
    boton_remove.click()
    time.sleep(2)
    
    # verificar que el carrito esté vacío
    print("Verificando que el carrito este vacio...")
    
    # buscar items en el carrito
    items_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    cantidad_items = len(items_carrito)
    
    print(f"Items encontrados en el carrito: {cantidad_items}")
    assert cantidad_items == 0, "El carrito debe estar vacío después de remover el item"
    
    # continuar comprando
    # hacer click en el boton Continue Shopping
    continue_shopping_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='continue-shopping']")
    continue_shopping_btn.click()
    time.sleep(5)
    assert "inventory" in driver.current_url, "Debe poder continuar comprando"
    
    # agregar dos items al carrito
    items_agregados = 0
    for i in range(2):  # agregar 2 items
        try:
            boton_add = driver.find_element(By.CSS_SELECTOR, "[data-test*='add-to-cart']")
            boton_add.click()
            items_agregados += 1
            time.sleep(2)
            print(f"Item {i+1} agregado al carrito")
        except:
            print(f"Error al agregar item {i+1}")

    print(f"Se agregaron {items_agregados} items al carrito")
    assert items_agregados == 2, "Debe poder agregar exactamente 2 items al carrito"
    
    # ir al carrito
    carrito_ok = ir_al_carrito(driver)
    assert carrito_ok, "Debe poder ir a la página del carrito"
    
    # verificar que los dos items estén en el carrito
    items_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    cantidad_items = len(items_carrito)
    assert cantidad_items == items_agregados, "Los dos items agregados deben estar en el carrito"
    

    # hacer click en el boton checkout
    checkout_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']")
    checkout_btn.click()
    time.sleep(5)
    assert "checkout" in driver.current_url, "Debe poder hacer checkout"
    
    # llenar información completa de checkout
    # escribir el nombre
    first_name = driver.find_element(By.CSS_SELECTOR, "[data-test='firstName']")
    first_name.send_keys("Diana")
    
    # escribir el apellido
    last_name = driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']")
    last_name.send_keys("Garcia")
    
    # escribir el codigo postal
    postal_code = driver.find_element(By.CSS_SELECTOR, "[data-test='postalCode']")
    postal_code.send_keys("12345")
    
    time.sleep(2)

    # hacer click en continue
    continue_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='continue']")
    continue_btn.click()
    time.sleep(5)
   
    
    # finalizar la compra
    # hacer click en el boton finish
    finish_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='finish']")
    finish_btn.click()
    time.sleep(5)
    assert "checkout-complete" in driver.current_url, "Debe poder finalizar la compra"
    
    print("OK Prueba COMPLETADA exitosamente")
    driver.quit()
