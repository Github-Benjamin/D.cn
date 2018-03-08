#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time : 2018/2/7 10:52

def appid(id):
    for i in range(1,99):
        a = "%s,1,VIP%s,%s0"%(id,i,i)
        print a

appid(6305)