# coding:utf-8
import web
import json
from TapHero import TapHero
from QiBin import QiBin
from QueryData import TestData

urls = (
    '/','Index',
    '/history','History',
    '/query','Query',
)

renter = web.template.render('templates')

class Index(object):
    def GET(self):

        TapHero_date = TapHero.date_list

        TapHero_cpu = TapHero.cpu_list
        TapHero_pss = TapHero.pss_list
        TapHero_fps = TapHero.fps_list
        TapHero_cpu_AverageDATA = TapHero.AverageDATA(TapHero_cpu)
        TapHero_pss_AverageDATA = TapHero.AverageDATA(TapHero_pss)
        TapHero_fps_AverageDATA = TapHero.AverageDATA(TapHero_fps)

        QiBin_cpu = QiBin.cpu_list
        QiBin_pss = QiBin.pss_list
        QiBin_fps = QiBin.fps_list
        QiBin_cpu_AverageDATA = TapHero.AverageDATA(QiBin_cpu)
        QiBin_pss_AverageDATA = TapHero.AverageDATA(QiBin_pss)
        QiBin_fps_AverageDATA = TapHero.AverageDATA(QiBin_fps)

        return renter.index(TapHero_cpu,TapHero_pss,TapHero_fps,TapHero_date,QiBin_cpu,QiBin_pss,QiBin_fps,TapHero_cpu_AverageDATA,TapHero_pss_AverageDATA,TapHero_fps_AverageDATA,QiBin_cpu_AverageDATA,QiBin_pss_AverageDATA,QiBin_fps_AverageDATA)


class History(object):
    def GET(self):

        data = web.input()
        deldate = str(data.get('deldate'))

        try:
            lists = deldate.split(",")
        except:
            lists = deldate
        if lists[0]!="None" and lists[0]!=None and lists[0]!='':
            print lists
            for delid in lists:
                if delid:
                    TestData.DeletData(delid)
            data = json.dumps({"success": '删除成功'})
            return data

        contrast = str(data.get('contrast'))
        try:
            lists = contrast.split(",")
        except:
            lists = contrast
        if len(lists)>2:
            return
        if lists[0]!="None" and len(lists)==2:
            for delid in lists:
                if delid:
                    TestData.DataLoad(delid)
            data = json.dumps({"success": '成功'})
            return data

        date = TestData.QueryDate()
        return renter.history(date)

    def POST(self):
        data = web.input()
        date = data.get('date')
        cpu = str(data.get('CPU'))
        fps = str(data.get('FPS'))
        pss = str(data.get('PSS'))

        if date and cpu and fps and pss:
            devicesdata = {"cpu":str(TestData.CheckData(cpu)),"fps":str(TestData.CheckData(fps)),"pss":str(TestData.CheckData(pss))}
            TestData.WriteData(date,devicesdata)

        raise web.seeother('/history')

class Query(object):
    def GET(self):

        data = web.input()

        contrast = str(data.get('contrast'))
        try:
            lists = contrast.split(",")
        except:
            lists = contrast
        if len(lists)>2:
            raise web.seeother('/history')
        if lists[0]!="None":
            try:

                one_name,two_name = lists[0],lists[1]
                one_cpu, one_fps, one_pss = TestData.DataLoad(lists[0])
                two_cpu, two_fps, two_pss = TestData.DataLoad(lists[1])

                one_cpu_AverageDATA, one_fps_AverageDATA, one_pss_AverageDATA = TestData.AverageDATA(one_cpu), TestData.AverageDATA(one_fps), TestData.AverageDATA(one_pss)
                two_cpu_AverageDATA, two_fps_AverageDATA, two_pss_AverageDATA = TestData.AverageDATA(two_cpu), TestData.AverageDATA(two_fps), TestData.AverageDATA(two_pss)

                datalist = []
                a = 0
                for i in list(eval(str(one_cpu))):
                    a += 1
                    datalist.append(a)
                return renter.contrast(datalist, one_cpu, one_fps, one_pss,two_cpu, two_fps, two_pss,one_cpu_AverageDATA, one_fps_AverageDATA, one_pss_AverageDATA,two_cpu_AverageDATA, two_fps_AverageDATA, two_pss_AverageDATA,one_name,two_name)
            except:
                raise web.seeother('/history')

        date = data.get('date')
        if date:
            cpu, fps, pss = TestData.DataLoad(date)
        else:
            cpu, fps, pss = 0,0,0

        cpu_AverageDATA,fps_AverageDATA,pss_AverageDATA =   TestData.AverageDATA(cpu),TestData.AverageDATA(fps),TestData.AverageDATA(pss)

        datalist = []
        a = 0
        for i in list(eval(str(cpu))):
            a += 1
            datalist.append(a)

        return renter.query(datalist,cpu,fps,pss,date,cpu_AverageDATA,fps_AverageDATA,pss_AverageDATA)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()