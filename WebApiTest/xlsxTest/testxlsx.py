# -*- coding:utf-8 -*-
import xlrd

data = xlrd.open_workbook('C:\\Users\\admin\\Desktop\\test.xlsx','r')

# 读取文件表名称
table = data.sheet_by_name(u'Sheet1')

# 获取行数和列数
nrows = table.nrows
ncols = table.ncols

# 循环行列表数据
datalist = []
for i in range(nrows):
    datalist.append(table.row_values(i))

namelist = {}
for i in range(len(datalist)):
    if i>3:
        namelist[datalist[i][1]]=i

checkname = raw_input("please input name:").decode("utf-8")

if checkname in namelist.keys():
    # 本人第20行
    tester = []
    closetime = []
    for i in  datalist[namelist.get(checkname)]:
        if i:
            data = i.split('\n')
            if len(data)>1:
                closetime.append(data[-2])
                worktime = data[-2].split(':')
                hour = int(worktime[0])-18
                if hour>0:
                    minute = int(worktime[1])-30
                    if minute>=0:
                        datatime = hour*60+minute
                        tester.append(datatime)
                    if minute<0:
                        datatime = hour * 60 + int(worktime[1])
                        tester.append(datatime)
                if hour==0:
                    minute = int(worktime[1]) - 30
                    if minute>0:
                        datatime = minute
                        tester.append(datatime)
        datanum = 0
        for i in tester:
            datanum +=i
    print "打卡次数%s，最后打开时间列表：%s"%(len(closetime),closetime)
    print "加班时长：%s时%s分"%(datanum/60,datanum%60)
else:
    print "查无数据"