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


class TestLogin(unittest.TestCase):

    # 必须使用 @classmethod 装饰器,所有test运行前运行一次
    @classmethod
    def setUpClass(cls):
        print('start setup')

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



    # 执行登陆操作，同一个用户短时间内连续登陆出现验证码，程序报错
    def CheckLogin(self):

        print("CheckLogin")
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
            self.driver.find_element_by_id(login.verifys).click()
            self.driver.find_element_by_id(login.input_verifys).send_keys("test")
            print("verifys verifys verifys !!!")
        except:
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



    # 用例1 打开APP冒烟检查
    def test_Login_CheckApp(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.index).click()
        print ('Login_CheckApp')



    # 用例2 检查登陆情况 点击消息
    def test_Login_click_message(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.message).click()
        print('click message')
        self.CheckLogin()
        

    # 用例3 检查登陆情况 点击下载
    def test_Login_click_download(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.download).click()
        print('click download')
        self.CheckLogin()



    # 用例4 检查登陆情况 点击列表下载
    def test_Login_click_downnload_btn(self):
        time.sleep(3)
        # 点击下载
        self.driver.find_elements_by_id(public.downnload_btn)[0].click()
        print('click downnload_btn')
        self.CheckLogin()



    # 用例5 检查登陆情况 点击详情页下载
    def test_Login_click_detail_downnload_btn(self):
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

        self.CheckLogin()


    # 用例6 检查index，登陆享受折扣按钮，检查登陆状态
    def test_Login_click_index_mygame(self):
        time.sleep(3)
        self.driver.find_element_by_id(index.mygame).click()
        print('click index_mygame')
        time.sleep(1)
        self.CheckLogin()
        
        

    # 用例7 检查登陆情况
    def test_Login_click_category(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.category).click()
        print('click category')
        # 点击下载
        time.sleep(3)
        self.driver.find_elements_by_id(public.downnload_btn)[0].click()
        print('click downnload_btn')
        self.CheckLogin()



    # 用例8 点击分类列表详情页下载检查 检查登陆情况
    def test_Login_click_category_detail_downnload_btn(self):
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

        self.CheckLogin()



    # 用例9 检查登陆情况 点击充值检查
    def test_Login_click_charge(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.charge).click()
        print('click charge')
        self.CheckLogin()
        


    # 用例10 检查登陆情况 个人界面
    def test_Login_click_personal_loginregister(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')
        self.driver.find_element_by_id(personal.not_login).click()
        print('click personal.not_login')
        self.CheckLogin()



    # 用例11 检查登陆情况 订单管理
    def test_Login_click_personal_order_manager(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')
        self.driver.find_element_by_id(personal.order_manager).click()
        print('click personal.order_manager')
        self.CheckLogin()



    # 用例12 检查登陆情况 下载管理
    def test_Login_click_personal_download_namager(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')
        self.driver.find_element_by_id(personal.download_namager).click()
        print('click personal.download_namager')
        self.CheckLogin()



    # 用例13 检查登陆情况 安全中心
    def test_Login_click_personal_personal_security(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')
        self.driver.find_element_by_id(personal.personal_security).click()
        print('click personal.personal_security')
        self.CheckLogin()

# if __name__ == '__main__':
    # 执行所有以test开头的用例
    # unittest.main()
    # # 初始化
    # suite = unittest.TestSuite()
    #
    # 添加单条测试用例
    # suite.addTest(TestLogin('test_Login_CheckApp'))
    # suite.addTest(TestLogin('test_Login_click_message'))
    # suite.addTest(TestLogin('test_Login_click_download'))
    # suite.addTest(TestLogin('test_Login_click_downnload_btn'))
    # suite.addTest(TestLogin('test_Login_click_detail_downnload_btn'))
    # suite.addTest(TestLogin('test_Login_click_index_mygame'))
    # suite.addTest(TestLogin('test_Login_click_category'))
    # suite.addTest(TestLogin('test_Login_click_category_detail_downnload_btn'))
    # suite.addTest(TestLogin('test_Login_click_charge'))
    # suite.addTest(TestLogin('test_Login_click_personal_loginregister'))
    # suite.addTest(TestLogin('test_Login_click_personal_order_manager'))
    # suite.addTest(TestLogin('test_Login_click_personal_download_namager'))
    # suite.addTest(TestLogin('test_Login_click_personal_personal_security'))

    # 生成测试报告
    # timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    # filename = timestr+'AutoTest.html'
    # fp = open(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='result',description='report')
    # runner.run(suite)
    # fp.close()

