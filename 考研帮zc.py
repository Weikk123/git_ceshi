#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Time : 2022/9/20 16:23
# @File : 考研帮zc.py
# @Software: PyCharm

# import time
# from appium import webdriver
# from selenium.webdriver.common.by import By
#
# caps={
#     'platformName':'Android',
#     'platformVersion':'5.1.1',
#     'deviceName':'127.0.0.1:62001',
#     'appPackage':'com.tal.kaoyan',
#     'appActivity':'com.tal.kaoyan.ui.activity.SplashActivity',
#     'noReset':False,
#     'unicodeKeyboard':True,
#     'resetKeyboard':True
# }
# driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
# driver.implicitly_wait(35)
# driver.find_element(By.ID,'tv_skip').click() #id定位点击跳过
# driver.find_element(By.ID,'tip_commit').click()  #点击同意
# # driver.find_element(By.ID,'login_email_edittext').send_keys('a1231342')
# # driver.find_element(By.ID,'login_password_edittext').send_keys('b12143wse')
# # driver.find_element(By.ID,'login_login_btn').click()  #点击登录
# driver.find_element(By.ID,'login_register_text').click()#点击注册
# driver.find_element(By.ID,'activity_register_username_edittext').send_keys('wxx524326')#输入用户名
# driver.find_element(By.ID,'activity_register_password_edittext').send_keys('wk524326')#输入密码
# driver.find_element(By.ID,'activity_register_email_edittext').send_keys('jsk@kdsew6kl.163.com')#输入邮箱
# driver.find_element(By.ID,'activity_register_register_btn').click()#点击立即注册
# driver.find_element(By.ID,'activity_perfectinfomation_time').click()#点击选择届
# #点击2019届
# driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]').click()
# driver.find_element(By.ID,'activity_perfectinfomation_major').click()#点击选择目标专业
# #点击哲学
# driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.TextView').click()
# #点击马克思主义哲学
# driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[3]/android.widget.TextView').click()
# driver.find_element(By.ID,'activity_perfectinfomation_school').click()#点击选择目标院校
# driver.tap([(117,1071)],1500)#根据坐标点击添加院校
# #点击北京
# driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
# #点击北京大学
# driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[2]/android.widget.TextView').click()
# time.sleep(5)
# driver.tap([(669,955)],1500)#根据坐标点击确定
# driver.find_element(By.ID,'activity_perfectinfomation_goBtn').click()#点击进入考研帮