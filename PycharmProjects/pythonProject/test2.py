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
# #无痕模式
# options.add_argument('--incognito')
# driver = webdriver.Chrome(chrome_options=options)
# driver = webdriver.Chrome(chrome_options=options)
# driver = webdriver.Chrome()
# driver.get("https://xenapp.cloudchalupa.com/")
# time.sleep(3)
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)
print(driver.current_url)
print(driver.title)

# 登录输入密码
driver.find_element(by=By.ID,value='username').send_keys('hao.zhang@citrix.com')
driver.find_element(by=By.ID,value='password').send_keys('Nice123!@#')
driver.find_element(by=By.ID,value="submit").click()

# 选择customer登录
driver.find_element('xpath','/html/body/div[2]/div/div/div/section/div/section[2]/div/div/div/section/input').send_keys('dil2xdestg1')
driver.find_element('xpath','/html/body/div[2]/div/div/div/section/div/section[2]/div/div/div/ol/li').click()
time.sleep(10)

# 最大化桌面截图
driver.maximize_window()
driver.find_element('xpath','/html/body/app/navbar/div/div/ul[1]/li[1]/a').click()
time.sleep(20)
driver.get_screenshot_as_file("C:\\JT\\a11.png")
time.sleep(2)


#下滑截图（需完善）
target = driver.find_element('xpath','/html/body/app/main/div/overview/div/overview-xae/div/div[4]/h3')
driver.execute_script("arguments[0].scrollIntoView();",target)
driver.get_screenshot_as_file("C:\\JT\\a16.png")
# time.sleep(2)
# driver.get_screenshot_as_file("C:\\JT\\a12.png")
#
# driver.find_element('xpath','/html/body/app/navbar/div/div/ul[1]/li[2]/a[1]').click()
# time.sleep(2)
# driver.get_screenshot_as_file("C:\\JT\\a13.png")
#
# driver.find_element('xpath','/html/body/app/navbar/div/div/ul[1]/li[3]/a').click()
# time.sleep(2)
# driver.get_screenshot_as_file("C:\\JT\\a14.png")
#
# #更换customer登录
# driver.find_element(by=By.ID,value="username-icon-standard").click()
# time.sleep(2)
# # driver.find_element(by=By.ID,value="ctx-navbar").click()
# driver.find_element('xpath','//*[@id="ctx-navbar"]/div[4]/div[2]/div/div/div/div[2]/div[1]/button').click()


# # 选择customer登录
# driver.find_element('xpath','/html/body/div/div/div/div/section/div/section[2]/div/div/div/section/input').click()
# driver.find_element('xpath','/html/body/div/div/div/div/section/div/section[2]/div/div/div/section/input').send_keys('stagetest4az')
# driver.find_element('xpath','/html/body/div/div/div/div/section/div/section[2]/div/div/div/ol/li/h2').click()
# time.sleep(60)

driver.find_element('xpath','//*[@id="ctx-navbar"]/div[1]/div[1]/ctx-icon[1]/div/div').click()
time.sleep(2)
driver.find_element('xpath','//*[@id="ctx-navbar"]/div[1]/div[2]/div[3]/a/span[2]').click()
time.sleep(2)
driver.find_element('xpath','//*[@id="ctx-navbar"]/div[1]/div[2]/div[4]/a/span').click()
time.sleep(20)
driver.get_screenshot_as_file("C:\\JT\\a16.png")


#更换customer登录
driver.find_element(by=By.ID,value="username-icon-standard").click()
time.sleep(2)
# driver.find_element(by=By.ID,value="ctx-navbar").click()
driver.find_element('xpath','//*[@id="ctx-navbar"]/div[4]/div[2]/div/div/div/div[2]/div[1]/button').click()
#

#选择customer登录
driver.find_element('xpath','/html/body/div/div/div/div/section/div/section[2]/div/div/div/section/input').click()
driver.find_element('xpath','/html/body/div/div/div/div/section/div/section[2]/div/div/div/section/input').send_keys('dilessstg9')
driver.find_element('xpath','/html/body/div/div/div/div/section/div/section[2]/div/div/div/ol/li/h2').click()
time.sleep(20)
driver.find_element('xpath','//*[@id="ctx-navbar"]/div[1]/div[1]/ctx-icon[1]/div/div').click()
time.sleep(2)
driver.find_element('xpath','//*[@id="ctx-navbar"]/div[1]/div[2]/div[3]/a/span[2]').click()
time.sleep(2)
driver.find_element('xpath','//*[@id="ctx-navbar"]/div[1]/div[2]/div[4]/a/span').click()
time.sleep(20)
driver.get_screenshot_as_file("C:\\JT\\a15.png")

target = driver.find_element('xpath','/html/body/app/main/div/overview/div/overview-xae/div/div[4]/h3')
driver.execute_script("arguments[0].scrollIntoView();",target)
driver.get_screenshot_as_file("C:\\JT\\a16.png")

