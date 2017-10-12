# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("http://115.182.62.11:81/")

        self.assertIn(u"任务跟踪系统", driver.title)

        # 设置Cookie
        # cookie = {'name':'Benjamin','value':'123'}
        # driver.add_cookie(cookie)
        # print driver.get_cookies()
        # 点击登陆按妞

        elem = driver.find_element_by_xpath('//*[@id="account"]/ul/li[1]/a')
        elem.click()

        # 输入用户名密码
        username = driver.find_element_by_name('username')
        username.send_keys("qiang.qian@downjoy.com")
        password = driver.find_element_by_name('password')
        password.send_keys('Qianqiang~123')

        # 点击的登陆按妞
        driver.find_element_by_name('login').click()
        time.sleep(1)
        assert u"qiang.qian@downjoy.com" in driver.page_source

        driver.save_screenshot('loginsucess.png')

        print driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/ul/li[1]/a').text
        print driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/ul/li[1]/a').get_attribute('value')
        # select 元素选择
        select = Select(driver.find_element_by_name('project_quick_jump_box'))
        # 获取所有select选项
        options = select.options
        for option in options:
            print option.get_attribute("value")
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()