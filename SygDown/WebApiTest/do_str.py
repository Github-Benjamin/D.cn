#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Benjamin 
# @Time : 2018/3/7 10:54
import re

# 用户处理fiddler抓取的header头字符串为指定规则

strs = '''
par_sig: f40b5753c349a881b73bcdac3d7e2e7a
ss: 1080x1920
sov: 2.0
sign: 2ce26dec2bbe3ac8
mid: 
versionCode: 100
accessToken: 
appid: 8412
pf: 1
User-Agent: Dalvik/2.1.0 (Linux; U; Android 5.1; m3 note Build/LMY47I) Syg/1.0.0
guildId: 105680
di: d7a06cb0a86ec312bf9dc97528701b8d
pushcid: 
stamp: 1520476606757
emu: 0
sinfo: uYiO5fLsh7Gxipfu9_SlBvju5AfEuvMM0_WnDczc4xvbGPTO19q31tppug0cDR7u2NDBJyLduzblC8Ty9PPVN-nMzCko-cbq9h3ONQQ3Ifs=
local: zh_CN
version: 1.0.0
language: zh
udid: 25496768e87599aab208fba48393bfde
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Host: api.sygdown.com
Connection: Keep-Alive
Accept-Encoding: gzip
Content-Length: 11
'''

setdata = ''

for i in strs.split("\n"):
    if i != None or i != "" or i!= '':
        data = i.split("\n")
        if data[0] != None or data[0]!= '' or data[0]!= '\n':
            twodata = data[0].split(": ")
            try:
                three = "'%s':'%s',\n"%(twodata[0],twodata[1])
                setdata +=three
            except:
                pass
print setdata