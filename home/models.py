# Create your models here.
# coding: UTF-8

import uuid
import os
import datetime
from django.db import models
from users.models import WechatProfile


class ExpressCompany(models.Model):
    express_id = models.CharField(max_length=50,
                               primary_key=True,
                               verbose_name="快递id")
    name = models.CharField(max_length=100, blank=True,
                            verbose_name="快递公司")
    price = models.CharField(max_length=100, blank=True,
                            verbose_name="价格")

    class Meta:
        verbose_name = "快递公司"
        verbose_name_plural = "快递公司"

    def __unicode__(self):
        return '%s' % (self.name)

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
    express = models.ForeignKey(ExpressCompany,
                               verbose_name="快递公司")
    file_obj = models.FileField(upload_to=datetime.datetime.now().strftime('uploadfile/cardlogo/%m-%Y'),
                                verbose_name="logo图案",blank=True)
    uploadtime = models.DateTimeField(blank=True, null=True,default=datetime.datetime.now(),
                                      verbose_name="创建时间")
    cardqian = models.FileField(upload_to=datetime.datetime.now().strftime('uploadfile/cardqian/%m-%Y'),
                                verbose_name="名片前面",blank=True)
    cardhou = models.FileField(upload_to=datetime.datetime.now().strftime('uploadfile/cardhou/%m-%Y'),
                                verbose_name="名片后面",blank=True)
    qrcode = models.CharField( verbose_name="二维码",blank=True,max_length=100)
    pic_head = models.FileField(upload_to=datetime.datetime.now().strftime('uploadfile/pichead/%m-%Y'),
                                verbose_name="头像",blank=True)

    class Meta:
        verbose_name = "电子名片"
        verbose_name_plural = "电子名片"

    def __unicode__(self):
        return '%s' % (self.name)



class ShippingAddress(models.Model):
    address_id = models.CharField(max_length=50,
                               primary_key=True, default=lambda:str(uuid.uuid4()),
                               verbose_name="收货地址id")
    wechatid = models.ForeignKey(WechatProfile,
                               verbose_name="微信用户ID")
    name = models.CharField(max_length=100, blank=True,
                            verbose_name="收货人")
    phone = models.CharField(max_length=100, blank=True,
                            verbose_name="联系方式")
    address = models.CharField(max_length=100, blank=True,
                            verbose_name="收货地址")

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = "收货地址"

    def __unicode__(self):
        return '%s' % (self.name)


