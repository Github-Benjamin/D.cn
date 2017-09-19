import random

def number():
    a = random.randint(0, 10000)
    return a

def lucky(a):
    if a<=1000: return '10%'
    if a>1000 and a<=3000: return '20%'
    if a>3000 and a<=5500: return '25%'
    if a>5500 and a<=9000: return '35%'
    if a>9000 and a<=9500: return '5%'
    if a>9500 and a<=9900: return '4%'
    if a>9900 and a<=10000: return '1%'

luckylist = []

for i in range(10000):
    a = lucky(number())
    luckylist.append(a)

dic = {}

for i in luckylist:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

print len(luckylist)
print luckylist
print dic

