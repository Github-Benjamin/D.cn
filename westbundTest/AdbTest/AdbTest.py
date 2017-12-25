# -*- coding: utf8 -*-
import os
import time
import threading

resultList = []
deviceText = os.popen('adb devices')

textList = deviceText.readlines()
deviceName = textList[1].split()[0]

def GetCPU():
    cpu = os.popen('adb shell top -n 1 -d 1|findstr com.westbund.heros.en').read()
    return cpu.split()[4]

def GetPSS():
    pss = os.popen('adb shell dumpsys meminfo|findstr com.westbund.heros.en').read()
    psslist = pss.split()[0].split(",")
    psstwo = psslist[1].split("K:")
    pss = "%s%s"%(psslist[0],psstwo[0])
    pss = "%sMb"%round(float(pss)/1024,2)
    return pss

def Times():
    times = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return times

def DevicesData():
    try:
        print Times(),GetCPU(),GetPSS()
    except:
        print "devices error! please check it"

DevicesData()

thread = ["Thread","Thread"]

while True:
    thread.append(threading.Thread(target=DevicesData, args=()))
    time.sleep(1)
    thread[-1].start()
