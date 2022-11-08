#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Time : 2022/9/23 15:11
# @File : cfg.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from appium import webdriver
from yaml读取 import get_yaml
import time

import allure


class Login():
    def __init__(self):
        self.drvier = webdriver.Remote('http://127.0.0.1:4723/wd/hub', get_yaml('b.yaml'))
        self.drvier.implicitly_wait(40)#隐式等待

    def denglu(self,username,passwd,mode=True):
        # self.drvier.find_element(By.ID, 'tv_skip').click()  # 根据id定位点击跳过
        # self.drvier.find_element(By.ID, 'tip_commit').click()  # 根据id定位点击同意
        # self.drvier.find_element(By.ID, 'login_email_edittext').send_keys(username)  # 输入用户名
        # self.drvier.find_element(By.ID, 'login_password_edittext').send_keys(passwd)  # 输入密码
        # self.drvier.find_element(By.ID, 'login_login_btn').click()  # 点击登录

        with allure.step('点击跳过'):
            self.drvier.find_element(By.ID, 'tv_skip').click()  # 根据id定位点击跳过
        with allure.step('点击同意'):
            self.drvier.find_element(By.ID, 'tip_commit').click()  # 根据id定位点击同意
        with allure.step('输入用户名'):
            self.drvier.find_element(By.ID, 'login_email_edittext').send_keys(username)  # 输入用户名
        with allure.step('输入密码'):
            self.drvier.find_element(By.ID, 'login_password_edittext').send_keys(passwd)  # 输入密码
        with allure.step('点击登录'):
            self.drvier.find_element(By.ID, 'login_login_btn').click()  # 点击登录

        if mode:
            time.sleep(3)
            # 获取每日热点text
            result = self.drvier.find_element(By.XPATH,
                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[1]').text
            # print(result)
            # assert result == '每日热点'
            return result
        else:
            time.sleep(3)
            data=self.drvier.find_element(By.ID,'login_login_btn').text
            # print('\n'+data)
            return  data

    def duankai(self):
        self.drvier.quit()#退出登录

if __name__ == '__main__':
    kaoyan=Login()
    kaoyan.denglu('a1231342','b12143wse')
    kaoyan.duankai()
