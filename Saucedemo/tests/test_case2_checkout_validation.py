#Este código fue realizado por Jackson Rojas
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import time

def test_checkout_validation(setup):
    driver = setup
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.login("standard_user", "secret_sauce")
    inventory.add_all_products_to_cart()
    inventory.go_to_cart()
    time.sleep(1)  # esperar que cargue el carrito

    assert cart.get_cart_items_count() > 0, "❌ El carrito está vacío"
