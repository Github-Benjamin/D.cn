#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Benjamin 
# @Time : 2018/3/8 19:16

from appium import webdriver
from Resource import Devices_config
from Resource import HTMLTestRunner
from Resource import public
from Resource import login
from Resource import detail
import unittest
import time


class Notlogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start setup')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',Devices_config.desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('tearDown')

    # 用例 1
    def Notlogin_CheckApp(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.index).click()
        print ('Notlogin_CheckApp')

    self.driver.find_element_by_id().click()
    # 用例2 检查未登录 点击消息
    def Notlogin_click_message(self):
        time.sleep(2)
        self.driver.find_element_by_id(public.message).click()
        print('click message')
        self.driver.find_element_by_id(login.back).click()
        print('click login.back')

    # 用例3 检查未登录 点击下载
    def Notlogin_click_download(self):
        time.sleep(2)
        self.driver.find_element_by_id(public.download).click()
        print('click download')
        self.driver.find_element_by_id(login.back).click()
        print('click login.back')

    # 用例4 检查未登录 点击列表下载
    def Notlogin_click_downnload_btn(self):
        time.sleep(2)
        self.driver.find_element_by_id(public.downnload_btn)[0].click()
        print('click downnload_btn')
        self.driver.find_element_by_id(login.back).click()
        print('click login.back')

    # 用例5 检查未登录 点击详情页下载
    def Notlogin_click_downnload_btn(self):
        time.sleep(2)
        self.driver.find_element_by_id(public.game_name)[0].click()
        print('click game_name')
        self.driver.find_element_by_id(detail.download)[0].click()
        print('detail.download')
        self.driver.find_element_by_id(login.back).click()
        print('click login.back')
        self.driver.find_element_by_id(detail.cancel).click()
        print('click detail.cancel')


if __name__ == '__main__':


    # 初始化
    suite = unittest.TestSuite()

    # 添加测试用例
    suite.addTest(Notlogin('test_sleep'))
    suite.addTest(Notlogin('test_clicktap1'))
    suite.addTest(Notlogin('test_clicktap2'))

    # 生成测试报告
    timestr = (time.strftime('%Y-%m-%d %X',time.localtime(time.time()))).split()
    filename = 'AutoTest.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='result',description='report')
    runner.run(suite)
    fp.close()

