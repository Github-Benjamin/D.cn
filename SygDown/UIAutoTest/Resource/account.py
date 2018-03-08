#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time : 2018/3/6 20:07
from Devices_config import *

not_login = appPackage+":id/layout_not_login"

# 登陆后
username = appPackage+":id/tv_personal_username"
quit = appPackage+":id/tv_personal_quit"
charge = appPackage+":id/tv_personal_recharge"

# 我的游戏
game = appPackage+":id/layout_personal_game"
game_count = appPackage+":id/tv_personal_recharge_game_count"
game_content = appPackage+":id/layout_personal_game_content"

# 订单管理 支付状态、支付金额、支付原价&折扣价格
order_manager = appPackage+":id/tv_personal_order_manager"
pay_status = appPackage+":id/tv_pay_status"
pay_price = appPackage+":id/tv_pay_price"
pay_discount = appPackage+":id/tv_pay_discount"
# 订单号、时间、游戏名称、支付方式
order_num = appPackage + ":id/tv_order_num"
order_time = appPackage + ":id/tv_order_time"
order_game_name = appPackage + ":id/tv_order_game_name"
order_pay_way = appPackage + ":id/tv_order_pay_way"

# 下载管理、安全中心
download_namager = appPackage+":id/tv_personal_download_namager"
personal_security  = appPackage+":id/tv_personal_security"

# 投诉建议
feedback = appPackage+":id/tv_personal_feedback"
feedback_content = appPackage+":id/ed_content"
feedback_word_count = appPackage+":id/tv_word_count"

# 该弹出层后无法选择界面无其他元素，需要点击其中一个
# 选择联系方式按钮
feedback_type = appPackage+":id/sp_contact_type"
# 联系方式列表 手机号、QQ、微信、邮箱
feedback_tv_type = appPackage+":id/tv_type"
# 输入联系方式
feedback_contact = appPackage+":id/ed_contact"
feedback_btn = appPackage+":id/tv_submit"

# 清理缓存
cache_size = appPackage+":id/tv_personal_cache_size"

# 关于我们
about_us = appPackage+":id/layout_personal_about_us"
version_up = appPackage+":id/tv_version_up"
version = appPackage + ":id/tv_version"
