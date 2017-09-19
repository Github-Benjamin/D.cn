# -*- coding:utf-8 -*-
import requests
import re

tags = '2,'

url = 'http://gift.d.cn/hd/recommand/game/by/tags'
# f = file('config','r').read()

header = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'28',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':f,
'Host':'gift.d.cn',
'Origin':'http://gift.d.cn',
'Referer':'http//gift.d.cn/hd/gameActivity/gotoWebsite.html?activityId=351',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}

data = {
'tags':tags,
'activityId':'351',
}

html = requests.post(url=url,data=data,headers=header).text
gameid = re.findall(r'''http://3g.d.cn/(.*?)"''',html)
page = re.findall(r'<span>(.*?)</span>',html)

# gameid = ['3456','1234','5454','3434']

try:
    date = ''
    b = 0
    for i in gameid:
        b += 1
        print b
        if i:
            date += str(i)+':'+str(i)+','
    f = file('gameconfig','w')
    f.write(date)
    f.close()
    print 'write sucess'
except Exception,e:
    print e
    print 'error'

