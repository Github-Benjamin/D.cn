# coding:utf-8
import web
from TapHero import TapHero
from QiBin import QiBin

urls = (
    '/','Index',
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

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()