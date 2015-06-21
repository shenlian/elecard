# coding: UTF-8
from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import User

from const.models import *


class WechatProfile(models.Model):
    wechatid = models.CharField( unique=True,max_length=100,
                               verbose_name="微信用户ID")

    class Meta:
        verbose_name = "微信用户"
        verbose_name_plural = "微信用户"

    def __unicode__(self):
        return '%s' % (self.wechatid)
