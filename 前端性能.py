#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Time : 2022/9/16 9:51
# @File : 前端性能.py
# @Software: PyCharm


#获取考研帮的CPU使用率
# import os
# a=os.popen('adb shell dumpsys cpuinfo | findstr com.tal.kaoyan')
# print(a.read())
# print(type(a.read()))
# a=os.popen('adb shell dumpsys cpuinfo | findstr com.tal.kaoyan')
# print(a.read().split(' ')[2])

# import os
# import time
# class Getcpu():
#     def get_cpu(self):
#         a=os.popen('adb shell dumpsys cpuinfo | findstr com.tal.kaoyan')
#         cpu=a.read().split(' ')[2]
#         now_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
#         #当前时间＋CPU使用率
#         self.cpu1=f'当前时间{now_time},CPU占用率为{cpu}\n'
#         # print(self.cpu1)
#
#     def save_cpu(self):
#         with open('cpu.txt','a',encoding='utf-8')as f:
#             f.write(self.cpu1)
#
#     def run(self,num):
#         for i in range(num):
#             self.get_cpu()
#             self.save_cpu()
#             time.sleep(2)#设置每次获取CPU占用率的时间
#
# aa=Getcpu()
# # aa.get_cpu()
# aa.run(3)


#统计考研帮APP流量消耗---获取接受和上传总和保存两位小数，单位：mb
# import time
# import os
# class Getzijie():
#     def get_zijie0(self):
#         a=os.popen('adb shell cat /proc/2462/net/dev')
#         zijie_info0=a.read().split('wlan0:')
#         # print(zijie_info[1])
#         zijie_info01=zijie_info0[1].split(' ')[2]
#         #print(zijie_info01)
#     def get_zijie1(self):
#         a=os.popen('adb shell cat /proc/2462/net/dev')
#         zijie_info1=a.read().split('wlan0:')
#         zijie_info11=zijie_info1[1].split(' ')[45]
#         #print(zijie_info11)
#     def get_zijie2(self):
#         a=os.popen('adb shell cat /proc/2462/net/dev')
#         zijie_info2=a.read().split('eth1:')
#         zijie_info21=zijie_info2[1].split(' ')[2]
#         #print(zijie_info21)
#     def get_zijie3(self):
#         a=os.popen('adb shell cat /proc/2462/net/dev')
#         zijie_info3=a.read().split('eth1:')
#         zijie_info31=zijie_info3[1].split(' ')[44]
#         #print(zijie_info31)




#统计考研帮APP内存消耗---实际物理内存占用情况
#分别统计5次冷启动和热启动的平均耗时，单位：s
# import time
# import os
# class Count_time():
#     def get_TotalTime(self):
#         cmd = os.popen('adb shell am start -W -n com.tal.kaoyan/.ui.activity.SplashActivity')
#         result = cmd.readlines()[8].replace('\n','').split(':')[1].replace(' ','')
#         TotalTime = int(result)
#         # print(TotalTime)
#         # print(type(TotalTime))
#         return TotalTime
#
#     def stop_app(self,mode):
#         if mode == 'hot':
#             os.popen('adb shell input keyevent 3')
#         elif mode == 'cold':
#             os.popen('adb shell am force-stop com.tal.kaoyan')
#
#     def get_avgtime(self,count_num,mode):
#         time_list = []
#         for i in range(count_num):
#             result1 = self.get_TotalTime()
#             print(f"第{i+1}次{mode}启动耗时{result1/1000}秒")
#             time_list.append(result1)
#             time.sleep(5)
#             self.stop_app(mode)
#             time.sleep(5)
#         else:
#             print(time_list)
#             avg_num = float((sum(time_list)/count_num)/1000)
#             print("平均%s启动耗时%.2f秒" %(mode,avg_num))
#
#     def run(self):
#         mod = input("冷热启动测试，请输入模式---hot 热启动测试，cold 冷启动测试：")
#         count_num = int(input("请输入测试次数："))
#         if mod == 'hot':
#             input("热启动测试，请确保app已经打开并退到后台\n回车继续...")
#             self.get_avgtime(count_num,mod)
#         elif mod == 'cold':
#             input("冷启动测试，请确保app没有打开\n回车继续...")
#             self.get_avgtime(count_num, mod)
#
#
# aa = Count_time()
# aa.run()




import time
from appium import webdriver
from selenium.webdriver.common.by import By
caps = {
"platformName": "Android",   # 被测手机是安卓
"platformVersion": "5.1.1",   # 手机安卓版本
"deviceName": "127.0.0.1:62001",   # 设备名
"appPackage": "com.tal.kaoyan",    # 启动APP Package名称
"appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",   	# 启动Activity名称
"noReset": False,   # 重置App
"unicodeKeyboard": True,  # 使用自带输入法，输入中文时填True
"resetKeyboard": True}  # 执行完程序恢复原来输入法
#   连接模拟器并驱动考研帮app---连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps) #远程连接
driver.implicitly_wait(20) #隐式等待
driver.find_element(By.ID,'tv_skip').click()  #id定位点击跳过
driver.find_element(By.ID,'tip_commit').click()  #点击同意
driver.find_element(By.ID,'login_email_edittext').send_keys('a1231342')
driver.find_element(By.ID,'login_password_edittext').send_keys('b12143wse')
# driver.find_element(By.ID,'login_login_btn').click()  #点击登录
