# coding=utf-8
from appium import webdriver
import time

# 滑动函数
def swipeDo(x1,y1,x2,y2,t=1000):
    x1 = x1
    y1 = y1
    y2 = y2
    driver.swipe(x1, y1, x2, y2,t)

desired_caps = {
    'platformName': 'Android',
    'deviceName': '2008edbdb51c',
    'platformVersion': '4.4',
    'appPackage': 'com.diguayouxi',
    'appActivity': 'com.diguayouxi.ui.FirstActivity',
    'newCommandTimeout':20,
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

def login(username):
    # 点击个人,然后登陆
    driver.find_element_by_id("com.diguayouxi:id/home_rb_mainpage_discovery").click()
    driver.find_element_by_id("com.diguayouxi:id/login_account").click()
    driver.find_element_by_id("com.diguayouxi:id/dcn_name").send_keys(username)
    driver.find_element_by_id("com.diguayouxi:id/dcn_password").send_keys("123456")
    driver.find_element_by_id("com.diguayouxi:id/dcn_login").click()
    # 调用Back
    driver.press_keycode(4)

def logout():
    # 点击个人
    driver.find_element_by_id("com.diguayouxi:id/home_rb_mainpage_discovery").click()
    driver.find_element_by_id("com.diguayouxi:id/to_account_center_iv").click()
    driver.find_element_by_id("com.diguayouxi:id/menu_more").click()
    driver.find_elements_by_android_uiautomator("new UiSelector().text(\"退出登录\")")[0].click()
    driver.find_element_by_id("com.diguayouxi:id/positive_button").click()

def comment():
    driver.find_elements_by_android_uiautomator("new UiSelector().text(\"飞刀又见飞刀\")")[0].click()
    driver.find_elements_by_android_uiautomator("new UiSelector().text(\"评论\")")[0].click()
    driver.find_element_by_id("com.diguayouxi:id/comment_text").click()
    driver.find_element_by_id("com.diguayouxi:id/comment_text").send_keys("This is auto comment! RObot007 hahaha  hehehehe heiheihei 001")
    driver.find_element_by_id("com.diguayouxi:id/publish_comment").click()

# 休眠20秒等待页面加载完成
time.sleep(20)

for i in range(3):
    time.sleep(1)
    swipeDo(300,900,300,300)

login("test10")
driver.press_keycode(4)
driver.find_element_by_id("com.diguayouxi:id/home_rb_mainpage_game").click()
comment()
logout()

