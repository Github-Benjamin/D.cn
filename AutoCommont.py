# -*- coding:utf-8 -*-
import requests
import ssl
import urllib2
import cookielib
import urllib
import re
import time
import threading
import random



def GetLoginCookie(user):

    url = "https://oauth.d.cn/auth/login"

    ssl._create_default_https_context = ssl._create_unverified_context

    data = {
        'to':'http%3A%2F%2Fmy.d.cn%2Fmember%2Fmy',
        't':'',
        'businessCode':'',
        'name':'%s'%user,
        'pwd':'b2927281520eba726728c6f5e9579228a3102f1462c52d708ba8ee622b2124a97545d0e3a6d0315bd84e457e7550ab2357e3c019fe23bf4a57ab2ead172d2e9ce8ae1e167d54a4530a200ba9be5b2fbe08b7cbfe07f914c3c09ccfa37488cc531f9452f625e0195ab41ec88546378ae304f5f774aa2de8891446ff77aae799d8',
		'geetest_challenge':'',
        'geetest_validate':'',
        'geetest_seccode':''
    }

    login_data = urllib.urlencode(data)

    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    response=opener.open(url,login_data)

    print response.read()
    cookies = response.headers["Set-Cookie"]

    print cookies

    reg = re.compile(r'''(AMBI=.*?;)''')
    AMBI = re.findall(reg,cookies)[0]

    reg = re.compile(r'''(_AES=.*?;)''')
    _AES = re.findall(reg,cookies)[0]

    reg = re.compile(r'''(_ev=.*?;)''')
    _ev = re.findall(reg,cookies)[0]

    reg = re.compile(r'''(djtk=.*?;)''')
    djtk = re.findall(reg,cookies)[0]

    reg = re.compile(r'''(DJ_MEMBER_INFO=.*?;)''')
    DJ_MEMBER_INFO = re.findall(reg,cookies)[0]

    Cookie = AMBI+_AES+_ev+djtk+DJ_MEMBER_INFO

    header = {
        'Accept':'*/*c',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Content-Length':'108',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':"%s"%Cookie,
        'Host':'ng.d.cn',
        'Origin':'http://ng.d.cn',
        'Referer':'http://ng.d.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }
    return header


def DoCommint(user,appid,commint):

    header =  GetLoginCookie(user)

    url = "http://ng.d.cn/comment/addcomment.html"

    data = {
        'rid':appid,
        'rtype':'5',
        'cmnt':str(commint),
        'atUser':''
    }

    html = requests.post(url=url,headers=header,data=data).text

    if "errorMsg" in html:
        return 0
    if len(html)>16:
        print "threading failed"
    else:
        return 1


def TCommint(user,appid,commint):
    DoCommint(user, appid, commint)

users = ["test01","test02","test03","test04","test05","test06"]


while True:

    # threads = []
    #
    # for user in users:
    #     num = random.randint(432, 7727)
    #     threads.append(threading.Thread(target=TCommint, args=(user,num , '用户：%s，游戏ID：%s，测试自动评论脚本，Autor：Benjamin，AutoTestCommint!'%(user,num))))
    #     # DoCommint(i, 6525, "用户：%s，测试自动评论脚本，嘿嘿嘿，穿越火线游戏应用"%i)
    #
    # for t in threads:
    #     t.start()
    # t.join()

    num = random.randint(432, 7727)
    TCommint("40179",num,'用户：Kali，游戏ID：%s，测试自动评论脚本，Autor：Benjamin，AutoTestCommint!'%num)
    print "sucess"
    time.sleep(31)


# for i in range(1,10):
#     if i > 9:
#         data = i
#     else:
#         data = "0%s" % i
#     print DoCommint("test%s"%data,6525,"测试自动评论脚本，嘿嘿嘿，穿越火线游戏应用")
