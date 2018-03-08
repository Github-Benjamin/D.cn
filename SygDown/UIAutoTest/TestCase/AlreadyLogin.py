#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Benjamin 
# @Time : 2018/3/8 19:16

from appium import webdriver
import unittest
import time

class AlreadyLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start setup')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '91QEBNQ2S2TM'
        desired_caps['appPackage'] = 'com.sygdown.market'
        desired_caps['appActivity'] = 'com.sygdown.ui.FirstActivity'
        desired_caps['newCommandTimeout'] = '30'
        desired_caps['platformVersion'] = '5.1'
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('tearDown')

    # 用例 1
    def AlreadyLogin_sleep(self):
        time.sleep(5)
        print('sleep passed')
        print ('do nothing')

    # 用例2 点击首页
    def AlreadyLogin_clicktap1(self):
        time.sleep(5)
        self.driver.find_element_by_id('com.sygdown.market:id/home_rb_mainpage_index').click()
        print('click index')

    # 用例3 点击分类
    def AlreadyLogin_clicktap2(self):
        time.sleep(5)
        self.driver.find_element_by_id('com.sygdown.market:id/home_rb_mainpage_category').click()
        print('click category')


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(AlreadyLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)
