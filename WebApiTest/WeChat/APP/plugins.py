#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Benjamin 
# @Time : 2018/3/26 14:58
from APP import models



# 检查菜单类型并添加dict
def CheckButton(ButtonNum):
    button = models.MenuInfo.objects.filter(button=ButtonNum)

    if button:

        if button[0].level == '1':
            strs = {"type": button[0].type, "name": button[0].name,"id":button[0].id}
            if button[0].key:
                strs["key"] = button[0].key
            if button[0].url:
                strs["url"] = button[0].url
            return strs

        if button[0].level == '2':
            strs = {"name": button[0].name,"id":button[0].id}

            buttoninfo = models.MenuInfo.objects.filter(buttontype=ButtonNum,button=0)

            sub_button = []
            CheckNum = 0
            for i in buttoninfo:

                if CheckNum>=5:
                    break

                sub_strs = {"type": i.type, "name": i.name,"id":i.id}
                if i.type == "view":
                    sub_strs["url"] = i.url
                if i.type == "click":
                    sub_strs["key"] = i.key
                sub_button.append(sub_strs)

                CheckNum +=1

            strs["sub_button"] = sub_button
            return strs



# 依次遍历检查菜单数据
def Buttons():

    button = []

    for i in range(1,4):
        if CheckButton(i):
            button.append(CheckButton(i))

    return button