# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MenuInfo(models.Model):
    type = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100,null=True)
    key = models.CharField(max_length=100,null=True)
    url = models.CharField(max_length=100,null=True)
    button = models.CharField(max_length=100, null=True)
    level = models.CharField(max_length=100, null=True)
    buttontype = models.CharField(max_length=100,null=True)
    createtime = models.DateTimeField(auto_now_add=True,null=True)
    uptime = models.DateTimeField(auto_now=True,null=True)