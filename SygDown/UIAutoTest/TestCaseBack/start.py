#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time : 2018/3/6 20:07

# from appium import webdriver
# from Resource.Devices_config import *
# import time
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


from Resource import HTMLTestRunner
import unittest
import time
import TestNotLogin
import TestPublicCase
import TestLogin
import TestAlreadyLogin

# 创建测试用例集
def allTest():
    suite1 = unittest.TestLoader().loadTestsFromModule(TestNotLogin)
    suite2 = unittest.TestLoader().loadTestsFromModule(TestPublicCase)
    suite3 = unittest.TestLoader().loadTestsFromModule(TestAlreadyLogin)
    suite4 = unittest.TestLoader().loadTestsFromModule(TestLogin)
    alltests=unittest.TestSuite([suite1,suite2,suite3,suite4])
    return alltests

if __name__=="__main__":
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    filename = timestr + 'AutoTest.html'
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                               title='SygDown AutoTest Report',
                                               description='Author Benjamin.',
                                               verbosity=2
                                               )
        runner.run(allTest())