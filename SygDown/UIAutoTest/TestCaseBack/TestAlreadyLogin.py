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
from Resource import category
from Resource import charge
import unittest
import time
import random
import os

class TestAlreadyLogin(unittest.TestCase):

    # 必须使用 @classmethod 装饰器,所有test运行前运行一次
    @classmethod
    def setUpClass(cls):
        os.system("adb shell pm clear com.sygdown.market")
        print('start setup')

    # 必须使用 @classmethod装饰器, 所有test运行完后运行一次
    @classmethod
    def tearDownClass(cls):
        print('tearDown')

    # 每个测试用例执行之前做操作
    def setUp(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Devices_config.desired_caps)
        print('install app')

    # 每个测试用例执行之后做操作
    def tearDown(self):
        self.driver.quit()
        print('quit app')

    # 公共方法
    def PublicSale(self):
        game = self.driver.find_elements_by_id(public.game_sale)[0]
        print("game_sale:%s"%game.text)
        game.click()
        print("click game")

        # 获取详情页游戏名称
        detail_name = self.driver.find_element_by_id(detail.name).text
        print ("detail.name:%s"%detail_name)

        # 获取详情页折扣信息
        detail_game_sale = self.driver.find_element_by_id(detail.discount_content)
        print("detail_game_sale:%s"%detail_game_sale.text)
        detail_game_sale.click()
        print("click detail_game_sale")

        # 折扣说明内嵌页
        time.sleep(1)
        webview_close = self.driver.find_element_by_id(public.webview_close).text
        self.assertEqual(webview_close, u"关闭")
        print ('assert webview_close')
        self.driver.find_element_by_id(public.webview_back).click()
        print ('click public.webview_back')

        # 折扣页充值页面
        time.sleep(1)
        self.driver.find_element_by_id(detail.charge).click()
        # 获取窗口标题 充值
        abs_title = self.driver.find_element_by_id(public.abs_title).text
        self.assertEqual(abs_title,u"充值")
        print("Assert True")

    # 首先登陆app
    def test_111(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.message).click()
        print('click message')
        print("Auto Login")
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

    # 用例 1 登陆点击消息检查
    def test_AlreadyLogin_message(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.message).click()
        print('click AlreadyLogin_message')

        # 获取窗口标题 消息中心
        abs_title = self.driver.find_element_by_id(public.abs_title).text
        self.assertEqual(abs_title,u"消息中心")
        print("Assert True")

    # 用例2 登陆点击下载检查
    def test_AlreadyLogin_download(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.download).click()
        print('click AlreadyLogin_download')

        # 获取窗口标题 下载管理
        abs_title = self.driver.find_element_by_id(public.abs_title).text
        self.assertEqual(abs_title,u"下载管理")
        print("Assert True")

    # 用例3 登陆点击我的游戏检查
    def test_AlreadyLogin_index_mygame(self):
        time.sleep(3)
        self.driver.find_element_by_id(index.mygame).click()
        print('click AlreadyLogin_index_mygame')

        # 获取窗口标题 我的游戏
        abs_title = self.driver.find_element_by_id(public.abs_title).text
        self.assertEqual(abs_title,u"我的游戏")
        print("Assert True")

    # 用例4 登陆后index页面折扣信息检查
    def test_AlreadyLogin_index_game_sale(self):
        time.sleep(3)
        print('click AlreadyLogin_index_game_sale')
        self.PublicSale()

    # 用例5 登陆后分类筛选折扣信息
    def test_AlreadyLogin_category_txt_filter(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.category).click()
        print ('click category')
        time.sleep(1)
        self.driver.find_element_by_id(category.txt_filter).click()
        print ('click category.txt_filter')

        # 获取分类列表
        txt_name = self.driver.find_elements_by_id(category.txt_name)[1]
        txt_name_name = txt_name.text
        print ('click txt_name_name:%s'%txt_name_name)
        txt_name.click()
        print ('click txt_name')
        time.sleep(3)

        self.PublicSale()

    # 用例6 登陆后点击充值
    def test_AlreadyLogin_charge(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.charge).click()
        print ('click public.charge')

        # 获取窗口标题 充值
        abs_title = self.driver.find_element_by_id(public.abs_title).text
        self.assertEqual(abs_title,u"充值")
        print("Assert True")

        # 获取充值账号
        user_name  = self.driver.find_element_by_id(charge.user_name).text
        print('user_name:%s'%user_name)

    # 用例7 点击个人 订单管理
    def test_AlreadyLogin_personal_order_manager(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')
        self.driver.find_element_by_id(personal.order_manager).click()
        print('click personal.order_manager')

        # 获取窗口标题 我的订单
        abs_title = self.driver.find_element_by_id(public.abs_title).text
        self.assertEqual(abs_title,u"我的订单")
        print("Assert True")

    # 用例8 点击个人 下载管理
    def test_AlreadyLogin_personal_download_namager(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')
        self.driver.find_element_by_id(personal.download_namager).click()
        print('click personal.download_namager')

        # 获取窗口标题 下载管理
        abs_title = self.driver.find_element_by_id(public.abs_title).text
        self.assertEqual(abs_title,u"下载管理")
        print("Assert True")

    # 用例9 点击个人 安全中心
    def test_AlreadyLogin_personal_security(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')
        self.driver.find_element_by_id(personal.personal_security).click()
        print('click personal.personal_security')

        time.sleep(1)
        webview_close = self.driver.find_element_by_id(public.webview_close).text
        self.assertEqual(webview_close, u"关闭")
        print ('assert webview_close')
        self.driver.find_element_by_id(public.webview_back).click()
        print ('click public.webview_back')

    # 用例10 点击个人 充值
    def test_AlreadyLogin_personal_charge(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')

        self.driver.find_element_by_id(personal.charge).click()
        print ('click personal.charge')

        # 获取窗口标题 充值
        abs_title = self.driver.find_element_by_id(public.abs_title).text
        self.assertEqual(abs_title,u"充值")
        print("Assert True")

        # 获取充值账号
        user_name  = self.driver.find_element_by_id(charge.user_name).text
        print('user_name:%s'%user_name)

    # 用例10 点击个人 退出
    def test_Zend_AlreadyLogin_personal_quit(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')

        self.driver.find_element_by_id(personal.quit).click()
        print ('click personal.quit')

        self.driver.find_element_by_id(public.message).click()
        print('click message')
        print('CheckLoginPage')
        self.driver.find_element_by_id(login.back).click()
        print('click login.back')


# if __name__ == '__main__':
#
#     suite = unittest.TestLoader().loadTestsFromTestCase(AlreadyLogin)
#     unittest.TextTestRunner(verbosity=2).run(suite)

