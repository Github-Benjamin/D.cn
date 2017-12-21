# -*- coding:utf-8 -*-
import requests

def AddItems(WGid,itemid,Num):
    url = "http://54.193.9.72:5400/?cmd=item&value=%s&account=%s&id=%s"%(Num,WGid,itemid)
    print url
    html = requests.get(url).text
    if "success=true" in html:
        pass
    else:
        print "Userid:%s add error" % WGid

def AddHero(WGid,item):
    url = "http://54.193.9.72:5400/?cmd=hero&value=1&account=%s&structid=%s"%(WGid,item)
    html = requests.get(url).text
    if "success=true" in html:
        pass
    else:
        print "Userid:%s add error"%WGid

itemid = file("ItemId.txt","r")
itemid = itemid.readlines()

itemnum = file("ItemNum.txt","r")
itemnum = itemnum.readlines()

for x in range(1,21):
    if len(str(x)) == 1:
        xs = "0%s" % x
        WGid = "wg%s@qq.com" % xs
    else:
        WGid = "wg%s@qq.com" % x
    # print WGid

    # 按照id和物品数量添加，格式： userid id num
    # for i in itemid:
    #     data = i.split()
    #     AddItems(WGid, data[0 ], 3)

    # 添加英雄 ，格式：heroid
    # for i in itemid:
    #     AddHero(WGid,i.split()[0])

# 添加单个物品，格式：userid id num
WGid = "wg09@qq.com"
# AddItems(WGid,10001,30)

# 添加英雄 ，格式：heroid
for i in itemnum:
    data = i.split()
    AddItems(WGid, data[0], data[1])