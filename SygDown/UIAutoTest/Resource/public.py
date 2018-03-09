#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time : 2018/3/6 20:07
from Devices_config import *

# 顶部 信息 搜索 下载
message = appPackage+":id/home_toolbar_message"
search = appPackage+":id/toolbar_search_layout"
download = appPackage+":id/home_toolbar_download"

# webview控件搜索
webview_back = appPackage+":id/webview_back"
webview_close = appPackage+":id/webview_action_bar_close"
WebView_class = "android.webkit.WebView"

# 顶部 返回、标题、下载
abs_up = appPackage+":id/abs__up"
abs_title = appPackage+":id/abs__action_bar_title"
abs_download = appPackage+":id/go_downloading"

# 底部 首页 分类 充值 个人
index = appPackage+":id/home_rb_mainpage_index"
category = appPackage+":id/home_rb_mainpage_category"
charge = appPackage+":id/home_rb_mainpage_charge"
personal = appPackage+":id/home_rb_mainpage_account"

# 列表 游戏名称 游戏大小 概述 折扣 下载按钮
game_name = appPackage+":id/item_game_name"
game_size = appPackage+":id/item_game_size"
game_outline = appPackage+":id/item_game_outline"
downnload_btn = appPackage+":id/item_download_btn"

# 登陆后显示 具体折扣数数据
game_sale = appPackage+":id/item_game_sale"