import pytest
# import allure
# from selenium import webdriver
#
# def test_image():
#     driver = webdriver.Chrome()
#     driver.get("https://baidu.com")
#
# @pytest.fixture(scope="class")
# def driver():
#     d = test_image()
#     return d
#
# import pytest
#
#
# @pytest.fixture()
# def connect_db():
#     print("Connect Database in .......")
#     yield
#     print("Close Database out .......")
#
#
# def read_database(key: str):
#     p_info = {
#         "name": "zhangsan",
#         "address": "China Guangzhou",
#         "age": 99
#     }
#     return p_info[key]
#
#
# def test_count(connect_db):
#     assert read_database("name") == "zhangsan"

@pytest.fixture()
def postcode():
    return '010'


def test_postcode(postcode):
    assert postcode == '010'
