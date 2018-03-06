# -*- coding:utf-8 -*-
import requests

url = "http://androidadmin.d.cn:8080/smtpfbackend2/digua/console/add_edit_daily.html?navTabId=daily_recommendation"

header  = {
'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Content-Length':'270',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'JSESSIONID=2f78e648dba52e63b70a9c332d0a',
'Host':'androidadmin.d.cn:8080',
'Origin':'http://androidadmin.d.cn:8080',
'Referer':'http://androidadmin.d.cn:8080/smtpfbackend2/user/login.html',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'
}


for i in range(19):

    if i > 9:
        data = i
    else:
        data = "0%s" % i

    datas = {
        'id': '',
        'resourceId': '80410',
        'name': '寒刃2',
        'createdDate': '2017-03-03 10:15:25',
        'description': '一款简单而又自由的冒险游戏，这里整个世界都自玩家笔下描绘而成，主角是否帅气，世界是否美好，都取决于你的绘画水平。',
        'multimediaType': '1',
        'dailyGameImg': 'http://money.downjoy.com/oauth/resources/themes/default/images/login/pic09.jpg',
        'videoUrl': 'http://video.smartgame-down.com/Androidvideo/80707_FreeFire_20171117.mp4',
    }
    html = requests.post(url=url,headers=header,data=datas).text
    print html


