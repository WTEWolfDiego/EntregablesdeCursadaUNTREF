#Este código fue realizado por Jackson Rojas
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_all_products_to_cart(self):
        buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(),'Add to cart')]"))
        )
        for button in buttons:
            button.click()
        print("✅ Se agregaron", len(buttons), "productos al carrito")

    def go_to_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()

