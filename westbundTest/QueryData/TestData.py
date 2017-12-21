# coding:utf-8
import json
import string

def DataLoad(QueryDate):
    try:
        f = open("TestData.txt", "r").read()
        data = json.loads(f)
        data = data.get(str(QueryDate))
    except:
        try:
            f = open("QueryData/TestData.txt", "r").read()
            data = json.loads(f)
            data = data.get(str(QueryDate))
        except:
            data = None
    if data:
        cpu = data.get("cpu")
        fps = data.get("fps")
        pss = data.get("pss")
        return cpu,fps,pss
    else:
        return None

def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] < lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

# 求平均值
def AverageDATA(datalist, total=0.0):
    num = 0

    lists = []
    for i in str(datalist).split("[")[1].split("]")[0].split("',"):
        lists.append(i.split("'")[1])

    for item in lists:
        total += string.atof(item)
        num += 1
    return round((total / num),4)

def QueryDate():
    try:
        f = open("TestData.txt", "r").read()
    except:
        f = open("QueryData/TestData.txt", "r").read()
    data = json.loads(f)
    return bubble_sort(data.keys())

def DeletData(QueryDate):
    try:
        f = open("TestData.txt", "r").read()
    except:
        f = open("QueryData/TestData.txt", "r").read()
    data = json.loads(f)
    copydata = data.copy()
    try:
        del(data[str(QueryDate)])
        try:
            f = open("TestData.txt", "w+")
        except:
            f = open("QueryData/TestData.txt", "w+")
        data = json.dumps(data, indent=2, ensure_ascii=False)
        try:
            f.write(data)
        except:
            f.write(copydata)
        f.close()
    except:
        return None

def WriteData(key,writedata):
    try:
        f = open("TestData.txt", "r").read()
    except:
        f = open("QueryData/TestData.txt", "r").read()
    data = json.loads(f)
    copydata = data.copy()
    try:
        data[key] = writedata
        try:
            f = open("TestData.txt", "w+")
        except:
            f = open("QueryData/TestData.txt", "w+")
        data = json.dumps(data, indent=2, ensure_ascii=False)
        try:
            f.write(data)
        except:
            f.write(copydata)
        f.close()
    except:
        return None

def CheckData(data):
    lists = []
    for i in data.split("\n"):
        if i:
            lists.append(i.split("\t")[1].split("\r")[0])
    return lists