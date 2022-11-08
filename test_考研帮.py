#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Time : 2022/9/23 11:22
# @File : test_考研帮.py
# @Software: PyCharm
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.support.ui import WebDriverWait
from yaml读取 import get_yaml
from cfg import Login

import allure
import os

# @allure.feature('测试模块的名称---登录')
# @allure.story('可以写对用例的一些描述')
# class Test_login:
#     def setup(self):
#         self.drvier = webdriver.Remote('http://127.0.0.1:4723/wd/hub',get_yaml('b.yaml'))
#         self.drvier.implicitly_wait(40)#隐式等待
#     def teardown(self):
#         self.drvier.quit()#退出考研帮
#
#     @allure.title('用例标题---01')
#     @allure.description('用例描述---用户名密码正确，登陆成功')
#     def test_denglu01(self):
#         with allure.step('点击跳过'):
#             self.drvier.find_element(By.ID, 'tv_skip').click()  # 根据id定位点击跳过
#         with allure.step('点击同意'):
#             self.drvier.find_element(By.ID, 'tip_commit').click()  # 根据id定位点击同意
#         with allure.step('输入用户名'):
#             self.drvier.find_element(By.ID, 'login_email_edittext').send_keys('a1231342')  # 输入用户名
#         with allure.step('输入密码'):
#             self.drvier.find_element(By.ID, 'login_password_edittext').send_keys('b12143wse')  # 输入密码
#         with allure.step('点击登录'):
#             self.drvier.find_element(By.ID, 'login_login_btn').click()  # 点击登录
#         # 获取每日热点text
#         result = self.drvier.find_element(By.XPATH,
#                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[1]').text
#         print(result)
#         assert result == '每日热点'
#
# if __name__ == '__main__':
#     # 运行...文件，打印详细信息，产生报告所需要源文件放入temp目录
#     pytest.main(['test_考研帮.py','-sv','--alluredir','./temp'])
#     os.system("allure generate ./temp -o ./report --clean")#生成测试报告
#     """
#     allure generate 固定命令
#     ./temp 产生报告所需要源文件放入temp目录
#     -o  输出output
#     ./report  生成allure报告的路径
#     --clean  清空report路径下原来的测试报告
#     """




class Testlogin():
    def setup(self):
        self.login=Login()  #初始化，启动APP

    def teardown(self):
        self.login.duankai() #关闭APP

    @pytest.mark.parametrize("caseinfo",get_yaml('c.yaml'))
    def test_denglu(self,caseinfo):
        allure.dynamic.title(caseinfo['title'])
        allure.dynamic.description(caseinfo['detail'])
        # print(caseinfo)
        res=self.login.denglu(caseinfo['data']['username'],caseinfo['data']['passwd'],caseinfo['data']['mode'])
        assert res==caseinfo['res']['reason']

if __name__ == '__main__':
    # pytest.main(['test_考研帮.py','-sv'])
    pytest.main(['test_考研帮.py','-sv','--alluredir','./temp'])
    os.system("allure generate ./temp -o ./report --clean")#生成测试报告



