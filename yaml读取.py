#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Time : 2022/9/20 15:18
# @File : yaml读取.py
# @Software: PyCharm

import yaml
#yaml文件读取
def get_yaml(file_name):
    with open(file_name,encoding='gbk')as f:
        data=yaml.safe_load(f)#读取yaml文件中的数据
        return data
        # print(data)
        # print(type(data))
        # print(data['family']['children'][0]['age'])
if __name__ == '__main__':
    print(get_yaml('c.yaml'))


