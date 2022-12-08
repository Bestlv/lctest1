import code
import time
import pyotp
import re
import win32clipboard
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)
# driver.get("https://xenapp.cloudchalupa.com/")
print(driver.current_url)
print(driver.title)

