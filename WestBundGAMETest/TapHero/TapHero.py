import string

def CreateDATA(filename):
    listdata = []
    files = file(str(filename), "r")
    for i in files.readlines():
        listdata.append(i.split()[1])
    return listdata

def CreateDATE(filename):
    listdata = []
    files = file(str(filename), "r")
    for i in range(len(files.readlines())):
        listdata.append(i)
        # dates = i.split()[0].split("-")
        # listdata.append("%s:%s:%s"%(dates[3],dates[4],dates[5]))
    return listdata

def AverageDATA(datalist, total=0.0):
    num = 0
    for item in datalist:
        total += string.atof(item)
        num += 1
    return round((total / num),4)

date_list = CreateDATE("TapHero/cpu_com_westbund_heros_en.txt")
cpu_list = CreateDATA("TapHero/cpu_com_westbund_heros_en.txt")
pss_list = CreateDATA("TapHero/pss.txt")
fps_list = CreateDATA("TapHero/fps.txt")
