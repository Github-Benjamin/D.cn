import requests

data = {
"pageNo":'1',
"activityId":'351',
}

f = file('config','r').read()
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


url = 'http://gift.d.cn/hd/recommand/game/oldplayer/goback'

html = requests.post(url=url,data=data,headers=header).text
print html