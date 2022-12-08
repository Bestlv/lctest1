from selenium import webdriver

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://baidu.com")
    print(driver.current_url)
    print(driver.title)
    return