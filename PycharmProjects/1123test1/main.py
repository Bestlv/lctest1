# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pytest
import os
import allure
# # Press the green button in the gutter to run the script.
# @pytest.fixture(scope='function')
# def login():
#     print('模拟登陆操作')
#     yield
#     print('登陆完成')
#
# @allure.feature('购买a')
# def test_1(login):
#     '''购买物品a
#     '''
#     print('测试用例test_image')
# @allure.feature('购买b')
# def test_2():
#     '''购买物品b'''
#     print("测试用例test1")
if __name__ =="__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['testcase','-s','--alluredir', './temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report --clean')
