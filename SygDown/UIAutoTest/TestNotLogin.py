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
from Resource import index
from Resource import personal
import unittest
import time
import random
import os


class Notlogin(unittest.TestCase):

    # 必须使用 @classmethod 装饰器,所有test运行前运行一次
    @classmethod
    def setUpClass(cls):
        print('start setup')
        # cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',Devices_config.desired_caps)

    # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        print('tearDown')

    # 每个测试用例执行之前做操作
    def setUp(self):
        os.system("adb shell pm clear com.sygdown.market")
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Devices_config.desired_caps)
        print('install app')

    # 每个测试用例执行之后做操作
    def tearDown(self):
        self.driver.quit()
        print('quit app')

    # 检查是否为登陆页面
    def CheckLoginPage(self):
        print('CheckLoginPage')
        self.driver.find_element_by_id(login.back).click()
        print('click login.back')

    # 用例1 打开APP冒烟检查
    def test_Notlogin_CheckApp(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.index).click()
        print ('Notlogin_CheckApp')

    # 用例2 检查未登录 点击消息
    def test_Notlogin_click_message(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.message).click()
        print('click message')
        self.CheckLoginPage()

    # 用例3 检查未登录 点击下载
    def test_Notlogin_click_download(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.download).click()
        print('click download')
        self.CheckLoginPage()


    # 用例4 检查未登录 点击列表下载
    def test_Notlogin_click_downnload_btn(self):
        time.sleep(3)
        # 点击下载
        self.driver.find_elements_by_id(public.downnload_btn)[0].click()
        print('click downnload_btn')
        self.CheckLoginPage()

    # 用例5 检查未登录 点击详情页下载
    def test_Notlogin_click_detail_downnload_btn(self):
        num = random.randint(0, 2)
        time.sleep(3)
        # 获取列表游戏名称
        click_game = self.driver.find_elements_by_id(public.game_name)[num]
        click_game_name = click_game.text
        print ('clicke click_game:%s'%click_game_name)

        # 点击游戏名称
        click_game.click()
        print('click game_name')

        # 获取详情页游戏名称
        detail_name = self.driver.find_element_by_id(detail.name).text
        print ("detail.name:%s"%detail_name)

        # 断言
        self.assertEqual(click_game_name,detail_name)
        print ("Assert True")

        # 点击详情页下载
        self.driver.find_elements_by_id(detail.download)[0].click()
        print('detail.download')
        self.CheckLoginPage()
        self.driver.find_element_by_id(detail.cancel).click()
        print('click detail.cancel')

    # 用例6 检查index，登陆享受折扣按钮，检查登陆状态
    def test_Notlogin_click_index_mygame(self):
        time.sleep(3)
        self.driver.find_element_by_id(index.mygame).click()
        print('click index_mygame')
        time.sleep(1)
        self.CheckLoginPage()

    # 用例7 点击分类列表下载检查
    def test_Notlogin_click_category(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.category).click()
        print('click category')
        # 点击下载
        time.sleep(3)
        self.driver.find_elements_by_id(public.downnload_btn)[0].click()
        print('click downnload_btn')
        self.CheckLoginPage()

    # 用例8 点击分类列表详情页下载检查
    def test_Notlogin_click_category_detail_downnload_btn(self):
        num = random.randint(0, 3)
        time.sleep(3)
        self.driver.find_element_by_id(public.category).click()
        print('click category')
        time.sleep(3)
        # 获取列表游戏名称
        click_game = self.driver.find_elements_by_id(public.game_name)[num]
        click_game_name = click_game.text
        print ('clicke click_game:%s'%click_game_name)

        # 点击游戏名称
        click_game.click()
        print('click game_name')

        # 获取详情页游戏名称
        detail_name = self.driver.find_element_by_id(detail.name).text
        print ("detail.name:%s"%detail_name)

        # 断言
        self.assertEqual(click_game_name,detail_name)
        print ("Assert True")

        # 点击详情页下载
        self.driver.find_elements_by_id(detail.download)[0].click()
        print('detail.download')
        self.CheckLoginPage()
        self.driver.find_element_by_id(detail.cancel).click()
        print('click detail.cancel')

    # 用例9 检查未登录 点击充值检查
    def test_Notlogin_click_charge(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.charge).click()
        print('click charge')
        self.CheckLoginPage()

    # 用例10 检查未登陆 个人界面
    def test_Notlogin_click_personal_loginregister(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')
        self.driver.find_element_by_id(personal.not_login).click()
        print('click personal.not_login')
        self.CheckLoginPage()

    # 用例11 检查未登陆 订单管理
    def test_Notlogin_click_personal_order_manager(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')
        self.driver.find_element_by_id(personal.order_manager).click()
        print('click personal.order_manager')
        self.CheckLoginPage()

    # 用例12 检查未登陆 下载管理
    def test_Notlogin_click_personal_download_namager(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')
        self.driver.find_element_by_id(personal.download_namager).click()
        print('click personal.download_namager')
        self.CheckLoginPage()

    # 用例13 检查未登陆 安全中心
    def test_Notlogin_click_personal_personal_security(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')
        self.driver.find_element_by_id(personal.personal_security).click()
        print('click personal.personal_security')
        self.CheckLoginPage()

# if __name__ == '__main__':
    # 执行所有以test开头的用例
    # unittest.main()
    # # 初始化
    # suite = unittest.TestSuite()
    #
    # # 添加单条测试用例
    # suite.addTest(Notlogin('Notlogin_CheckApp'))
    # suite.addTest(Notlogin('Notlogin_click_message'))
    # suite.addTest(Notlogin('Notlogin_click_download'))
    # suite.addTest(Notlogin('Notlogin_click_downnload_btn'))
    # suite.addTest(Notlogin('Notlogin_click_detail_downnload_btn'))
    # suite.addTest(Notlogin('Notlogin_click_index_mygame'))
    # suite.addTest(Notlogin('Notlogin_click_category'))
    # suite.addTest(Notlogin('Notlogin_click_category_detail_downnload_btn'))
    # suite.addTest(Notlogin('Notlogin_click_charge'))
    # suite.addTest(Notlogin('Notlogin_click_personal_loginregister'))
    # suite.addTest(Notlogin('Notlogin_click_personal_order_manager'))
    # suite.addTest(Notlogin('Notlogin_click_personal_download_namager'))
    # suite.addTest(Notlogin('Notlogin_click_personal_personal_security'))
    #
    # # 生成测试报告
    # timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    # filename = timestr+'AutoTest.html'
    # fp = open(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='result',description='report')
    # runner.run(suite)
    # fp.close()
    #
