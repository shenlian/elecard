# Create your models here.
# coding: UTF-8

import uuid
import os
import datetime
from django.db import models

class ElectricCard(models.Model):
    card_id = models.CharField(max_length=50,
                               primary_key=True, default=lambda:str(uuid.uuid4()),
                               verbose_name="电子名片唯一ID")
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
    url = models.CharField(max_length=100, blank=True,
                            verbose_name="网址")
    address = models.CharField(max_length=100, blank=True,
                            verbose_name="社交帐号")
    social_account = models.CharField(max_length=100, blank=True,
                            verbose_name="社交帐号")
    profile = models.CharField(max_length=100, blank=True,
                            verbose_name="个人简介")
    custom = models.CharField(max_length=100, blank=True,
                            verbose_name="自定义")
    file_obj = models.FileField(upload_to=datetime.datetime.now().strftime('uploadfile/cardlogo/%m-%Y'),
                                verbose_name="logo图案")
    uploadtime = models.DateTimeField(blank=True, null=True,
                                      verbose_name="创建时间")