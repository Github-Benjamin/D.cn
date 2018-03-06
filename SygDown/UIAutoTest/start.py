#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time : 2018/3/6 20:07

from appium import webdriver
from Resource.Devices_config import *
import time

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


