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
from confest import test_c

class TestPvnet:
        def test_creat(self):
                options = webdriver.ChromeOptions()
                options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                driver = webdriver.Chrome(options=options)
                driver.maximize_window()
                # driver.find_element(by=By.ID, value="confirmCatalogDelete").click()
                # driver.find_element('class name', value="ctx-checkbox-label danger ng-star-inserted").click()
                driver.find_element(by=By.ID, value="ctx-accordion-group-header-4").click()
                driver.find_element(by=By.ID, value="daasDashboardAddConnections").click()
                driver.find_element(By.XPATH,'//*[//*[@id="cdk-overlay-19"]/ctx-blade/onprem-connection-setup-blade/div/button[1]').click()
                user = driver.find_element('xpath','//*[@id="cdk-overlay-16"]/ctx-blade/onprem-connection-setup-blade/div/button[1]/p[1]').text  # 获取搜索条目的文本信息。
                print(user)
                # assert c== "Add a network connection"