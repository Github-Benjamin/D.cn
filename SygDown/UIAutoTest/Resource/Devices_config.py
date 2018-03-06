#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time : 2018/3/6 20:07

# 启动服务命令 appium -a 127.0.0.1 -p 4723 –U 91QEBNQ2S2TM --no-reset
platformVersion = "platformVersion"
AppiumPort = 4723
appPackage = 'com.sygdown.market'

desired_caps = {
    # 设备系统
    'platformName': 'Android',
    'deviceName': '91QEBNQ2S2TM',
    'platformVersion': '5.1',

    # 包名和主Activity
    'appPackage': 'com.sygdown.market',
    'appActivity': 'com.sygdown.ui.FirstActivity',
    # 超时时间
    'newCommandTimeout':30,
}


