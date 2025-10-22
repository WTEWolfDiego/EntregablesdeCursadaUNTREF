#Este código fue realizado por Jackson Rojas
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items_count(self):
        items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
        )
        return len(items)

    def remove_first_item(self):
        buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Remove']"))
        )
        buttons[0].click()
        time.sleep(1)

    def continue_shopping(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue-shopping"))
        )
        button.click()
        time.sleep(1)
