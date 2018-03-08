#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Benjamin 
# @Time : 2018/3/7 10:52
import requests
import json

url = "http://api.sygdown.com/index/guild/list"

#ssl._create_default_https_context = ssl._create_unverified_context

header = {
    'par_sig': 'f40b5753c349a881b73bcdac3d7e2e7a',
    'ss': '1080x1920',
    'sov': '2.0',
    'sign': '2ce26dec2bbe3ac8',
    'mid': '',
    'versionCode': '100',
    'accessToken': '',
    'appid': '8412',
    'pf': '1',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1; m3 note Build/LMY47I) Syg/1.0.0',
    'guildId': '105680',
    'di': 'd7a06cb0a86ec312bf9dc97528701b8d',
    'pushcid': '',
    'stamp': '1520476606757',
    'emu': '0',
    'sinfo': 'uYiO5fLsh7Gxipfu9_SlBvju5AfEuvMM0_WnDczc4xvbGPTO19q31tppug0cDR7u2NDBJyLduzblC8Ty9PPVN-nMzCko-cbq9h3ONQQ3Ifs=',
    'local': 'zh_CN',
    'version': '1.0.0',
    'language': 'zh',
    'udid': '25496768e87599aab208fba48393bfde',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'api.sygdown.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'Content-Length': '11'
}

data = {
    'pn':'1',
    'ps':'20'
}

html = requests.post(url=url,headers=header,data=data)

data =  html.text
data = json.loads(data)


print data.get("msg"),data.get("code")
pagedata = data.get("data")

print "totalCount",pagedata.get("totalCount"),"\nlen(list)：",len(pagedata.get("list"))
