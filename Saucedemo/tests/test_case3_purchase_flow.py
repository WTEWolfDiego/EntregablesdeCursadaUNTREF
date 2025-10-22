#Este código fue realizado por Jackson Rojas
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import time

def test_complete_purchase_flow(setup):
    driver = setup
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.login("standard_user", "secret_sauce")
    inventory.add_all_products_to_cart()
    inventory.go_to_cart()
    time.sleep(1)

    cart.remove_first_item()
    cart.continue_shopping()

    # agregar 2 productos
    add_buttons = driver.find_elements("xpath", "//button[contains(text(),'Add to cart')]")
    add_buttons[0].click()
    add_buttons[1].click()
    inventory.go_to_cart()
    time.sleep(1)

    assert cart.get_cart_items_count() == 2, "❌ No se agregaron los 2 productos"

    checkout.start_checkout()
    checkout.enter_first_name("Jackson")
    checkout.enter_last_name("Rojas")
    checkout.enter_postal_code("1408")
    checkout.continue_checkout()
    checkout.finish_checkout()
