#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Time : 2022/9/21 10:09
# @File : 日志.py
# @Software: PyCharm

# import logging
# #使用basicConfig来定义输出---(level:来定义日志输出级别,filename:定义输出到哪个文件,filemode:定义输出模式,format:定义输出格式)
# logging.basicConfig(level=logging.DEBUG,filename='demo.log',filemode='w',format=('%(message)s|%(asctime)s|%(levelname)-8s|%(filename)s:%(lineno)d'))
# name='小明'
# age=18
# #向日志信息中输出变量
# logging.debug('姓名%s,年龄%d' %(name,age))
# logging.debug('姓名{},年龄{}'.format(name,age))
# logging.debug(f'姓名{name},年龄{age}')
# logging.debug('姓名%s,年龄%d',name,age)
# logging.debug('调试信息')
# logging.info('软件按照预期进行')
# logging.warning('软件运行到这里可能会进行报错')
# logging.error('软件已经不能执行一些功能了')
# logging.critical('软件已经无法继续运行了')



# import logging
# #记录器--Logger
# logger=logging.getLogger('ccc.applog')
# logger.setLevel(logging.DEBUG)
# print(logger)
# print(type(logger))
#
# #处理器--Handler
# #添加输出到控制台的处理器
# consolehandler=logging.StreamHandler()
# consolehandler.setLevel(logging.DEBUG)
# #添加输出到文件的处理器--如果没有设置日志级别,将使用Logger的日志级别
# filehandler=logging.FileHandler(filename='applog1.log')
# filehandler.setLevel(logging.INFO)
#
# #添加一个格式化器
# formatter=logging.Formatter('%(asctime)s|%(levelname)-8s|%(filename)s:%(lineno)d|%(message)s')
#
# #给处理器设置格式
# consolehandler.setFormatter(formatter)
# filehandler.setFormatter(formatter)
#
# #添加过滤器
# flt=logging.Filter('ccc')
# #记录器关联过滤器
# logger.addFilter(flt)
#
# #给记录器设置处理器
# logger.addHandler(consolehandler)
# logger.addHandler(filehandler)
#
# #打印日志
# name='小明'
# age=18
# #向日志信息中输出变量
# logger.debug('调试信息')
# logger.info('软件按照预期进行')
# logger.warning('软件运行到这里可能会进行报错')
# logger.error('软件已经不能执行一些功能了')
# logger.critical('软件已经无法继续运行了')




# import logging.config
# logging.config.fileConfig('log.conf')
#
# logger=logging.getLogger('applog')
# logger.debug('这是一个debug日志')






import logging
logger=logging.getLogger('heihei')
logger.setLevel('DEBUG')

conhandler=logging.StreamHandler()
conhandler.setLevel(logging.INFO)
# consolehandler=logging.StreamHandler()
# consolehandler.setLevel(logging.DEBUG)
filehander=logging.FileHandler('abb.log')

formatter=logging.Formatter('%(message)s')

conhandler.setFormatter(formatter)
filehander.setFormatter(formatter)

logger.addHandler(conhandler)
logger.addHandler(filehander)

logger.debug('调试信息')
logger.info('软件按照预期进行')
logger.warning('软件运行到这里可能会进行报错')
logger.error('软件已经不能执行一些功能了')
logger.critical('软件已经无法继续运行了')