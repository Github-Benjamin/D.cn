# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from APP import models
from plugins import *
from django.db.models import Q
import json

# Create your views here.
# Index
def Index(request):
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        # 签名，时间戳，目前，XML

        message = {
            "code":"200",
            "status":"scuess",
            "content": "index",
        }

        return HttpResponse(json.dumps(message))

    if request.method == 'POST':
        pass


# Menu
def Menu(request):
    if request.method == 'GET':

        # button 一级菜单 必须 1-3个
        # sub_button 二级菜单 非必须 1-5个
        # type 类型 必须 常用可选类型click,view,media_id,view_limited
        # name 必须 菜单标题 不超过16个字节
        # key 非必须 click类型必须 不超过128个字节
        # url 非必须 view类型必须 不超过1024字节
        # media_id 非必须 media_id与view_limited类型必须 调用新增永久素材接口返回的合法media_id

        type = request.GET.get('type')
        if type == "1":
            menu = {"button": Buttons()}
            return HttpResponse(json.dumps(menu))

        tree = models.MenuInfo.objects.filter(~Q(button='0'))
        relopermissions = models.MenuInfo.objects.filter(level=0)

        ret = {"tree":tree,"relopermissions":relopermissions}
        return render(request, 'menutree.html', {'ret': ret})

    if request.method == 'POST':

        # 增加一级菜单
        addmenuname = request.POST.get('addmenuname')
        if addmenuname:
            addtype = request.POST.get('addtype')
            type = request.POST.get('type')

            a = models.MenuInfo.objects.latest('button')
            b = int(a.button)+1

            if addtype == "click":
                models.MenuInfo(name=addmenuname,type=addtype,key=type,level=1,button=b,buttontype=b).save()
            if addtype == "view":
                models.MenuInfo(name=addmenuname,type=addtype,url=type,level=1,button=b,buttontype=b).save()
            if addtype == "0":
                models.MenuInfo(name=addmenuname,level=2,button=b,buttontype=b).save()

        # 增加二级菜单
        menuid = request.POST.get('menuid')
        if menuid:
            menuname = request.POST.get('menuname')
            addtype = request.POST.get('addtype')
            type = request.POST.get('type')
            if addtype == "click":
                models.MenuInfo(name=menuname,type=addtype,key=type,buttontype=menuid,button=0,level=0).save()
            if addtype == "view":
                models.MenuInfo(name=menuname, type=addtype, url=type, buttontype=menuid,button=0,level=0).save()


        # 修改一级菜单
        uponeid = request.POST.get('uponeid')
        if uponeid:
            upmenuname = request.POST.get('upmenuname')
            addtype = request.POST.get('addtype')
            type = request.POST.get('type')

            if addtype == "click":
                models.MenuInfo.objects.filter(id=uponeid).update(name=upmenuname,type=addtype,key=type,url="",level=1)
            if addtype == "view":
                models.MenuInfo.objects.filter(id=uponeid).update(name=upmenuname, type=addtype,key="",url=type,level=1)
            if addtype == "0":
                models.MenuInfo.objects.filter(id=uponeid).update(name=upmenuname, type="",key="",url="",level=2)

        # 修改二级菜单
        upid = request.POST.get('upid')
        if upid:
            upmenuname = request.POST.get('upmenuname')
            upmenuid = request.POST.get('upmenuid')
            addtype = request.POST.get('addtype')
            type = request.POST.get('type')

            if addtype == "click":
                models.MenuInfo.objects.filter(id=upid).update(name=upmenuname,type=addtype,key=type,url="",buttontype=upmenuid)
            if addtype == "view":
                models.MenuInfo.objects.filter(id=upid).update(name=upmenuname, type=addtype,key="",url=type,buttontype=upmenuid)

        # 删除菜单
        batchdelid = request.POST.get('batchdelid')
        if batchdelid:
            deletesql = models.MenuInfo.objects.extra(where=['id in (' + batchdelid + ')'])
            if deletesql.delete():
                return HttpResponse(json.dumps({"success": '删除成功'}))
            else:
                return HttpResponse(json.dumps({"error": '删除失败'}))

        return HttpResponseRedirect('/menu')


# KeyWord
def KeyWord(request):
    if request.method == 'GET':

        message = {
            "code":"200",
            "status":"scuess",
            "content":"keyword",
        }

        return HttpResponse(json.dumps(message))

    if request.method == 'POST':
        pass


# Test
def Test(request):
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass