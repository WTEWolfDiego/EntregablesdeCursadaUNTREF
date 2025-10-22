#Este código fue realizado por Jackson Rojas
import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
