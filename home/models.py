# Create your models here.
# coding: UTF-8

import uuid
import os
import datetime
from django.db import models
from users.models import WechatProfile

class ElectricCard(models.Model):
    card_id = models.CharField(max_length=50,
                               primary_key=True, default=lambda:str(uuid.uuid4()),
                               verbose_name="电子名片唯一ID")
    wechatid = models.ForeignKey(WechatProfile,
                               verbose_name="微信用户ID")
    name = models.CharField(max_length=100, blank=True,
                            verbose_name="姓名")
    company = models.CharField(max_length=100, blank=True,
                            verbose_name="公司")
    position = models.CharField(max_length=100, blank=True,
                            verbose_name="职位")
    phone = models.CharField(max_length=100, blank=True,
                            verbose_name="电话")
    email = models.CharField(max_length=100, blank=True,
                            verbose_name="邮箱")
    fox = models.CharField(max_length=100, blank=True,
                            verbose_name="传真")
    url = models.URLField(max_length=100, blank=True,
                            verbose_name="网址")
    address = models.CharField(max_length=100, blank=True,
                            verbose_name="地址")
    social_account = models.CharField(max_length=100, blank=True,
                            verbose_name="社交帐号")
    profile = models.CharField(max_length=1000, blank=True,
                            verbose_name="个人简介")
    custom = models.CharField(max_length=1000, blank=True,
                            verbose_name="自定义")
    file_obj = models.FileField(upload_to=datetime.datetime.now().strftime('uploadfile/cardlogo/%m-%Y'),
                                verbose_name="logo图案",blank=True)
    uploadtime = models.DateTimeField(blank=True, null=True,default=datetime.datetime.now(),
                                      verbose_name="创建时间")
