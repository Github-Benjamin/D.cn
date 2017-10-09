# coding=utf-8
from appium import webdriver
import time

# 滑动页面
#屏幕向上滑动
def swipeUp(t=1000):
    l = driver.get_window_size()
    x1 = int(l.get("width") * 0.5)
    y1 = int(l.get("height") * 0.75)
    y2 = int(l.get("height") * 0.25)
    driver.swipe(x1, y1, x1, y2,t)

#屏幕向下滑动
def swipeDown(t=1000):
    l = driver.get_window_size()
    x1 = int(l.get("width") * 0.5)
    y1 = int(l.get("height") * 0.25)
    y2 = int(l.get("height") * 0.75)
    driver.swipe(x1, y1, x1, y2,t)

desired_caps = {
    'platformName': 'Android',
    'deviceName': '2008edbdb51c',
    'platformVersion': '4.4',
    'appPackage': 'com.diguayouxi',
    'appActivity': 'com.diguayouxi.ui.FirstActivity',
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 休眠10秒等待页面加载完成
# 关闭更新弹窗
time.sleep(20)
swipeUp()
driver.find_element_by_id("com.diguayouxi:id/update_head_close").click()

# 点击发现
driver.find_element_by_id("com.diguayouxi:id/home_rb_mainpage_discovery").click()

userlogin = driver.find_element_by_id("com.diguayouxi:id/login_account").text
print "userlogin: " + userlogin

driver.find_element_by_id("com.diguayouxi:id/login_account").click()

# 输入用户名、密码并点击登陆
time.sleep(1)
driver.find_element_by_id("com.diguayouxi:id/dcn_name").send_keys("208040117")
driver.find_element_by_id("com.diguayouxi:id/dcn_password").send_keys("Qq350105629")
driver.find_element_by_id("com.diguayouxi:id/dcn_login").click()

# 登陆成功获取用户名
usernaame =  driver.find_element_by_id("com.diguayouxi:id/tv_username").text
print "username: " + usernaame

time.sleep(1)
swipeUp()
swipeDown()
swipeUp()
swipeDown()

# 取消退出登录
time.sleep(1)
driver.find_element_by_id("com.diguayouxi:id/menu_more").click()
driver.find_elements_by_android_uiautomator("new UiSelector().text(\"退出登录\")")[0].click()
driver.find_element_by_id("com.diguayouxi:id/negative_button").click()

# 确定退出登录
driver.find_element_by_id("com.diguayouxi:id/menu_more").click()
driver.find_elements_by_android_uiautomator("new UiSelector().text(\"退出登录\")")[0].click()
driver.find_element_by_id("com.diguayouxi:id/positive_button").click()

userlogin = driver.find_element_by_id("com.diguayouxi:id/login_account").text
print "userlogin: " + userlogin

driver.press_keycode(4)
driver.press_keycode(4)
driver.press_keycode(4)

# 退出
driver.quit()
