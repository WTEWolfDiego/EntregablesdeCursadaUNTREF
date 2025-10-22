#Este código fue realizado por Jackson Rojas
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def start_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    def enter_first_name(self, name):
        self.driver.find_element(By.ID, "first-name").send_keys(name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)

    def enter_postal_code(self, postal):
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)

    def continue_checkout(self):
        self.driver.find_element(By.ID, "continue").click()

    def finish_checkout(self):
        self.driver.find_element(By.ID, "finish").click()
