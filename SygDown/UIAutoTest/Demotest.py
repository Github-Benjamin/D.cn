#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time : 2018/3/8 16:21
from appium import webdriver
from Resource import Devices_config
from Resource import HTMLTestRunner
from Resource import public
from Resource import login
from Resource import detail
from Resource import index
from Resource import personal
import unittest
import time
import random
import os


class Dttest(unittest.TestCase):

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
    def test_sleep(self):
        time.sleep(5)
        print('sleep passed')
        print ('do nothing')

    # 用例2 点击首页
    def test_clicktap1(self):
        time.sleep(5)
        self.driver.find_element_by_id('com.sygdown.market:id/home_rb_mainpage_index').click()
        print('click index')

    # 用例3 点击分类
    def test_clicktap2(self):
        time.sleep(5)
        self.driver.find_element_by_id('com.sygdown.market:id/home_rb_mainpage_category').click()
        print('click category')

    # 首先登陆app
    def test_111(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.message).click()
        print('click message')
        print("Auto Login")
        time.sleep(1)
        self.driver.find_element_by_id(login.username_login).click()
        print("checck login_page")
        print("click login.username_login")

        self.driver.find_element_by_id(login.user_username).send_keys("Benjamin001")
        print("send_text user_username:Benjamin001")
        self.driver.find_element_by_id(login.user_passwd).send_keys("123456")
        print("send_text user_passwd:123456")

        for i in range(20):
            self.driver.find_element_by_id(login.user_username).click()
            time.sleep(3)
            print("time.sleep(3)")

        self.driver.find_element_by_id(login.user_login_btn).click()
        print("click user_login_btn")

        try:
            time.sleep(3)
            self.driver.find_element_by_id(login.verifys).click()
            self.driver.find_element_by_id(login.input_verifys).send_keys("test")
            print("verifys verifys verifys !!!")
        except:
            time.sleep(3)
            self.driver.press_keycode(4)
            print("click back")
            time.sleep(5)
            self.driver.press_keycode(4)
            print("click back")
            self.driver.find_element_by_id(public.personal).click()
            print("click public.personal")

            self.username = self.driver.find_element_by_id(personal.username).text
            print("username:%s"%self.username)
            self.assertEqual(self.username,"Benjamin001")
            print("Assert username")



if __name__ == '__main__':

    # 初始化
    suite = unittest.TestSuite()

    # 添加测试用例
    suite.addTest(Dttest('test_111'))

    # 生成测试报告
    timestr = (time.strftime('%Y-%m-%d %X',time.localtime(time.time()))).split()
    filename = 'AutoTest.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='result',description='report')
    runner.run(suite)
    fp.close()
