#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Benjamin 
# @Time : 2018/3/8 19:16

from appium import webdriver
from Resource import Devices_config
from Resource import HTMLTestRunner
from Resource import public
from Resource import category
from Resource import login
from Resource import detail
from Resource import index
from Resource import personal
import unittest
import time
import random


class Notlogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('start setup')

    @classmethod
    def tearDownClass(cls):
        print('tearDown')

    def setUp(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Devices_config.desired_caps)
        print('install app')

    def tearDown(self):
        self.driver.quit()
        print('quit app')

    # 用例1 打开APP冒烟检查
    def public_index(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.index).click()
        print ('public_index CheckAPP')

    # 用例2 点击首页搜索，然后返回
    def public_search(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.search).click()
        print ('click public.search')
        search_tv = self.driver.find_element_by_id('com.sygdown.market:id/search_tv').text
        self.assertEqual(search_tv,u"搜 索")
        print ('assert search_btn')
        self.driver.find_element_by_id('com.sygdown.market:id/back_iv').click()
        print ('click public.search')

    # 用例3 点击首页折扣说明检查内嵌页
    def public_index_sale_rules(self):
        time.sleep(3)
        self.driver.find_element_by_id(index.sale_rules).click()
        print ('click public.sale_rules')
        webview_close = self.driver.find_element_by_id(public.webview_close).text
        self.assertEqual(webview_close, u"关闭")
        print ('assert webview_close')
        self.driver.find_element_by_id(public.webview_back).click()
        print ('click public.webview_back')

    # 用例4 点击分类 类别塞选
    def public_category_txt_category(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.category).click()
        print ('click category')
        self.driver.find_element_by_id(category.txt_category).click()
        print ('click category.txt_category')

        num = random.randint(1, 12)
        # 获取分类列表
        txt_name = self.driver.find_elements_by_id(category.txt_name)[num]
        txt_name_name = txt_name.text
        print ('click txt_name_name:%s'%txt_name_name)
        txt_name.click()
        print ('click txt_name')

        # 点击详情页
        time.sleep(3)
        num = random.randint(0, 2)
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

        game_type = self.driver.find_element_by_id(detail.type).text
        print ("game_type:%s"%game_type)
        self.assertIn(txt_name_name, game_type)
        print ("Assert True")

    # 用例5 点击分类 类别开测时间 已经开测
    def public_category_txt_order(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.category).click()
        print ('click category')
        self.driver.find_element_by_id(category.txt_order).click()
        print ('click category.txt_order')

        # 获取分类列表
        txt_name = self.driver.find_elements_by_id(category.txt_name)[3]
        txt_name_name = txt_name.text
        print ('click txt_name_name:%s'%txt_name_name)
        txt_name.click()
        print ('click txt_name')

        time.sleep(3)
        # 获取列表游戏名称
        click_game = self.driver.find_elements_by_id(public.game_name)[0]
        click_game_name = click_game.text
        print ('clicke click_game:%s'%click_game_name)
        click_game.click()
        print('click game_name')

        # 获取详情页游戏名称
        time.sleep(1)
        detail_name = self.driver.find_element_by_id(detail.name).text
        print ("detail.name:%s"%detail_name)
        # 断言
        self.assertEqual(click_game_name,detail_name)
        print ("Assert True")

        # 滑动检查开服表
        self.driver.swipe(300,720,300,300,500)
        self.driver.find_element_by_id(detail.open_server)
        print('find detail.open_server')

    # 用例6 点击分类 类别折扣 无折扣
    def public_category_txt_filter(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.category).click()
        print ('click category')
        self.driver.find_element_by_id(category.txt_filter).click()
        print ('click category.txt_filter')

        # 获取分类列表
        txt_name = self.driver.find_elements_by_id(category.txt_name)[2]
        txt_name_name = txt_name.text
        print ('click txt_name_name:%s'%txt_name_name)
        txt_name.click()
        print ('click txt_name')
        time.sleep(3)

        # 获取列表游戏名称
        click_game = self.driver.find_elements_by_id(public.game_name)[0]
        click_game_name = click_game.text
        print('clicke click_game:%s'%click_game_name)

        try:
            print(self.driver.find_element_by_id(public.game_sale).text)
        except:
            print('True')

    # 用例7 点击个人 投诉建议
    def public_personal_feedback(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print ('click personal')
        self.driver.find_element_by_id(personal.feedback).click()
        print ('click personal.feedback')

        # 获取窗口标题 断言
        abs_title = self.driver.find_element_by_id(public.abs_title).text
        self.assertEqual(abs_title,u"投诉建议")

        # 随机选择联系方式
        self.driver.find_element_by_id(personal.feedback_type).click()
        num = random.randint(0,3)
        feedback_tv_type = self.driver.find_elements_by_id(personal.feedback_tv_type)[num]
        feedback_tv_type_name = feedback_tv_type.text
        print("feedback_tv_type_name:%s"%feedback_tv_type_name)
        feedback_tv_type.click()
        print("click feedback_tv_type")

        # 检查选择联系方式是否正确
        self.assertEqual(feedback_tv_type_name,self.driver.find_element_by_id(personal.feedback_tv_type).text)
        print("Assert select feedback_tv_type")

        # 发送投诉信息
        strs = ["phone","qq","wechat","email"]
        ContactsList = ["18081011501", "350105629", "Benjamin350", "Benjamin_v@qq.com"]
        self.driver.find_element_by_id(personal.feedback_content).send_keys("Select: "+strs[num]+str(ContactsList[num])+"\n\nBenjamin AutoTest")
        self.driver.find_element_by_id(personal.feedback_contact).send_keys(ContactsList[num])
        self.driver.find_element_by_id(personal.feedback_btn).click()
        time.sleep(3)
        print ('click personal.feedback:%s'%self.driver.find_element_by_id(personal.feedback).text)

    # 用例8 点击个人 清除缓存
    def public_personal_cache_size(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print ('click personal')

        cache_size = self.driver.find_element_by_id(personal.cache_size)
        cache_size_name = cache_size.text
        print("cache_size:%s"%cache_size_name)
        cache_size.click()
        print ("clicck cache_size")

        time.sleep(3)
        cache_size_name = cache_size.text
        print("cache_size:%s" % cache_size_name)
        self.assertEqual(cache_size_name,'0B')
        print("cache_size success")

    # 用例9 点击个人 关于我们
    def public_personal_about_us(self):
        time.sleep(3)
        self.driver.find_element_by_id(public.personal).click()
        print('click personal')

        self.driver.find_element_by_id(personal.about_us).click()
        print('click about_us')

        # 获取窗口标题 断言
        abs_title = self.driver.find_element_by_id(public.abs_title).text
        self.assertEqual(abs_title,u"关于")

        # 获取当前版本，升级检测
        version_up = self.driver.find_element_by_id(personal.version_up).text
        print("version_up:%s"%version_up)
        version = self.driver.find_element_by_id(personal.version).text
        print("version:%s"%version)


if __name__ == '__main__':


    # 初始化
    suite = unittest.TestSuite()

    # 添加单条测试用例
    suite.addTest(Notlogin('public_index'))
    suite.addTest(Notlogin('public_search'))
    suite.addTest(Notlogin('public_index_sale_rules'))
    suite.addTest(Notlogin('public_category_txt_category'))
    suite.addTest(Notlogin('public_category_txt_order'))
    suite.addTest(Notlogin('public_category_txt_filter'))
    suite.addTest(Notlogin('public_personal_feedback'))
    suite.addTest(Notlogin('public_personal_cache_size'))
    suite.addTest(Notlogin('public_personal_about_us'))

    # 生成测试报告
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    filename = timestr+'AutoTest.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='result',description='report')
    runner.run(suite)
    fp.close()

