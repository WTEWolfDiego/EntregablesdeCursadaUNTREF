#Este código fue realizado por Jackson Rojas
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_sort_products(setup):
    driver = setup
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")
    # Aquí va cualquier acción de sorting que se desee probar
    assert "inventory.html" in driver.current_url
