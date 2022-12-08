import code
import time
import pyotp
import re
import win32clipboard
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
options = webdriver.ChromeOptions()
#无痕模式
options.add_argument('--incognito')
driver = webdriver.Chrome(chrome_options=options)
# driver = webdriver.Chrome()
driver.get("https://xenapp.cloudchalupa.com/")
time.sleep(10)
##driver.implicitly_wait(3000);
driver.find_element(by=By.ID,value='username').send_keys('Ruyu.yin@citrix.com')
driver.find_element(by=By.ID,value='password').send_keys('Best234@#$')
driver.find_element(by=By.ID,value="submit").click()
time.sleep(40)
def get_token(my_secret):
    totp = pyotp.TOTP(my_secret)
    my_token = totp.now()

    print(my_token)
if __name__ == '__main__':
    get_token("BOK6AQMFCRISMLC6")

    # 打开粘贴
    win32clipboard.OpenClipboard()
    # 清空粘贴板
    win32clipboard.EmptyClipboard()
    # 设置复制的内容为Text
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT,)
    # 关闭粘贴板线程
    win32clipboard.CloseClipboard()
    # 打开粘贴板
    win32clipboard.OpenClipboard()
    # 获取粘贴板内容，传给参数data
    data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
    # 输出粘贴板内容
    print(data)
    # 需要关闭一下粘贴板线程
    win32clipboard.CloseClipboard()
driver.find_element('xpath', '//*[@id="mfa-login"]/div/div[1]/div[4]/div/input').click()
driver.find_element('xpath','//*[@id="mfa-login"]/div/div[1]/div[4]/div/input').send_keys(Keys.CONTROL, 'v')
# driver.find_element(by=By.NAME,value='0').send_keys(X);
driver.find_element(by=By.ID,value="verify-totp-code").click()
driver.find_element('xpath','/html/body/div[2]/div/div/div/section/div/section[2]/div/div/div/section/input').send_keys('ouj3lvucojxc')
driver.find_element('xpath','/html/body/app/navbar/div/div/ul[1]/li[1]/button').click()
time.sleep(15)
driver.find_element(by=By.ID,value="catalog-name-input-0").send_keys('QC')
driver.find_element('xpath','/html/body/app/main/div/overview/div/daas-overview/daas-ftu/div/div[1]/div[2]/div[2]').click()
#driver.quit()