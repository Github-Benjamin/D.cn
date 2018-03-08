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
    'deviceName': '91QEBNQ2S2TM',
    'platformVersion': '5.1',
    'appPackage': 'com.diguayouxi',
    'appActivity': 'com.diguayouxi.ui.FirstActivity',
    'newCommandTimeout':30,
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 休眠10秒等待页面加载完成
# 关闭更新弹窗
time.sleep(20)
try:
    driver.find_element_by_id("com.diguayouxi:id/update_head_close").click()
except:
    pass


# 滑动首屏Banner区域
# 左滑动
time.sleep(1)
for i in range(5):
    swipeDo(666,300,222,300)
# 右滑动
for i in range(5):
    swipeDo(222,300,666,300)

# 点击Banner区域
driver.find_element_by_id("com.diguayouxi:id/icon").click()
# 获取游戏名称
gamename = driver.find_element_by_id("com.diguayouxi:id/res_detail_name").text
print "gamename: " + gamename

# 点击游戏分享按钮
driver.find_element_by_id("com.diguayouxi:id/res_detail_share").click()
# 更多分享
driver.find_elements_by_android_uiautomator("new UiSelector().text(\"更多\")")[0].click()
# 调用Back
driver.press_keycode(4)


# 单游戏详情页上下滑动操作
time.sleep(1)
# 上滑6次操作
try:
    for i in range(12):
        swipeDo(200,940,200,500)
except:
    pass
# 下滑6次操作
try:
    for i in range(11):
        swipeDo(200,500,200,940)
    # 关闭详情页
    driver.find_element_by_id("com.diguayouxi:id/abs__up").click()
    # driver.find_element_by_id("com.diguayouxi:id/res_detail_cancel").click()
except:
    pass

try:
    # 滑动Tab选项区域
    # 左滑动
    time.sleep(1)
    swipeDo(666,700,200,700)
    swipeDo(666,700,200,700)
    # 右滑动
    swipeDo(200,700,666,700)
    swipeDo(200,700,666,700)
except:
    pass

# 点击顶部Tab选项，点击分类
driver.find_elements_by_android_uiautomator("new UiSelector().text(\"分类\")")[0].click()
# swipeDo(300,940,300,600)
driver.find_elements_by_android_uiautomator("new UiSelector().text(\"MOBA\")")[0].click()
# 依次点击同类下分类、热度排序、筛选
driver.find_element_by_id("com.diguayouxi:id/fl_category").click()
driver.find_element_by_id("com.diguayouxi:id/fl_order").click()
driver.find_element_by_id("com.diguayouxi:id/fl_filter").click()

# 返回到APP首页
driver.find_element_by_id("com.diguayouxi:id/abs__up").click()

# 搜索一款游戏
driver.find_element_by_id("com.diguayouxi:id/toolbar_search_layout").click()
driver.find_element_by_id("com.diguayouxi:id/input_auto_tv").send_keys("wangzherongyao")
driver.find_element_by_id("com.diguayouxi:id/search_tv").click()
time.sleep(3)
gamename = driver.find_element_by_id("com.diguayouxi:id/name").text
print "gamename: " + gamename
# 调用Back
driver.press_keycode(4)
driver.press_keycode(4)

# 点击网游
time.sleep(1)
driver.find_element_by_id("com.diguayouxi:id/home_rb_mainpage_net_game").click()
try:
   for i in range(5):
        time.sleep(2)
        swipeDo(700,700,100,700)
        for i in range(6):
            time.sleep(2)
            swipeDo(300, 900, 300, 500)
except:
    pass

# 点击原创
driver.find_element_by_id("com.diguayouxi:id/home_rb_mainpage_original").click()
try:
   for i in range(5):
        time.sleep(2)
        swipeDo(700,700,100,700)
        for i in range(6):
            time.sleep(2)
            swipeDo(300, 900, 300, 500)
except:
    pass

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
for i in range(4):
    swipeDo(300,900,300,600)
    swipeDo(300,600,300,900)

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

# 调用Back
driver.press_keycode(4)
driver.press_keycode(4)
driver.press_keycode(4)

# 退出
driver.quit()
