#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Time : 2022/9/19 15:03
# @File : 考研帮.py
# @Software: PyCharm
from appium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from yaml读取 import get_yaml
import logging.config
#
# caps = {
#   "platformName": "Android",
#   "platformVersion": "5.1.1",
#   "deviceName": "127.0.0.1:62001",
#   "appPackage": "com.tal.kaoyan",
#   "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
#   "noReset": False,
#   "unicodeKeyboard": True,
#   "resetKeyboard": True
# }
logging.config.fileConfig('log.conf')

logger=logging.getLogger('applog')
logger.info('连接模拟器并驱动考研帮APP')
# #连接模拟器并驱动考研帮APP
drvier = webdriver.Remote('http://127.0.0.1:4723/wd/hub',get_yaml('b.yaml'))
drvier.implicitly_wait(40)#隐式等待
logger.info('跳过启动动画')
# drvier.find_element(By.ID,'tv_skip').click()#根据id定位点击跳过
drvier.tap([(650,56)],20000)#根据坐标定位点击跳过

#当前页面中有多个相同的class元素时，可以使用drvier.find_elements()来获取到值相同的按钮放在一个列表里,再通过下标来获取到想要操作的按钮
# time.sleep(30)
# list1=drvier.find_elements(By.CLASS_NAME,'android.widget.TextView')
# print(list1)
# print(type(list1))
# print(len(list1))
# list1[3].click()
logger.info('点击同意用户隐私权限')
drvier.find_element(By.ID,'tip_commit').click()#根据id定位点击同意
logger.info('输入用户名')
drvier.find_element(By.ID,'login_email_edittext').send_keys('a1231342')#输入用户名
logger.info('输入密码')
drvier.find_element(By.ID,'login_password_edittext').send_keys('b12143wse')#输入密码
logger.info('点击登录')
drvier.find_element(By.ID,'login_login_btn').click()#点击登录
logger.info('点击我')
drvier.find_element(By.ID,'mainactivity_button_mysefl').click()#点击我
logger.info('点击>')
drvier.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView').click()#点击>
logger.info('点击本科院校')
#显示等待时间--为某个按钮专门设置等待时间
WebDriverWait(drvier,15).until(lambda x:x.find_element(By.ID,'activity_myinfo_bschooltextview'))
drvier.find_element(By.ID,'activity_myinfo_bschooltextview').click()#点击本科院校
#向各个方向的滑动---drvier.swipe()
size = drvier.get_window_size()#获取屏幕长和宽
# print(size)
x=size['width']
y=size['height']
logger.info('划出下方的本科院校')
#向下滑动---y轴从大到小
time.sleep(5)
def down(num,ti):
  for i in range(num):
    drvier.swipe(x*0.5,y*0.8,x*0.5,y*0.2,duration=ti)
down(3,1000)
#
# drvier.save_screenshot('1.png')
# #向上滑动---y轴从小到大
# for i in range(3):
#   drvier.swipe(x*0.5,y*0.2,x*0.5,y*0.8,duration=1000)

