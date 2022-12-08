import code
import time
import pyotp
import re
import pytest
import win32clipboard
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture(scope="function")
def test_c():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.find_element(by=By.ID, value="confirmCatalogDelete").click()
    print(driver.current_url)
    print(driver.title)
    yield driver
    time.sleep(2)
    # driver.quit()