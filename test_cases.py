#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Time : 2022/9/23 9:14
# @File : test_cases.py
# @Software: PyCharm
import pytest


class Test_lianxi():
    def setup_class(self):
        print('\n--开始初始化--')
    def teardown_class(self):
        print('\n--执行清除操作--')

    def test_C001001(self):
        print('用例C001001')
        assert 1 == 1  #做断言---判断预期结果与实际结果是否一致

    def test_C001002(self):
        print('用例C001002')
        assert 2 == 2

    # @pytest.mark.skip(reason='跳过的提示信息')
    @pytest.mark.skipif(2.5>2.0,reason='满足条件不执行改用例')#判断版本大于2.0，不执行该用例
    def test_C001003(self):
        print('用例C001003')
        assert 3 == 2

    @pytest.mark.parametrize("a,b",[(1,2),(0,3)])
    def test_C001004(self,a,b):
        print(a,b)

if __name__ == '__main__':
    pytest.main(['test_cases.py','-sv'])