# coding:utf-8
import requests
import random

a = 0
b = 0

def check_data(s):
    url = 'http://3g.d.cn/comment/newYearHotList.html?rtype=5&ps=20&pn=%s'%s
    global html
    html = requests.get(url).text
    return html

for i in range(100):
    s = random.randint(1, 10)
    if 'null' in check_data(s):
        print html
        b = b+1
    else:
        a = a+1

print '请求失败次数:%s'%b,'请求成功次数:%s'%a

