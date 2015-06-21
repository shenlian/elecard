#!/usr/bin/env python
# coding=utf-8
'''
 File Name: users/form.py
 Author: shenlian
 Created Time: 2014年05月30日 星期五 15时40分16秒
'''
from django import forms
from home.models import *

class ElectricCardForm(forms.ModelForm):
    class Meta:
        model = ElectricCard
        exclude = ('card_id','uploadtime','wechatid','express','cardqian','cardhou','qrcode')
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control","id":"ename","placeholder":"姓名"}),
            'company':forms.TextInput(attrs={'class':"form-control","id":"ecompany","placeholder":"公司"}),
            'position':forms.TextInput(attrs={'class':"form-control","id":"eposition","placeholder":"职位"}),
            'phone':forms.TextInput(attrs={'class':"form-control","id":"ephone","placeholder":"电话"}),
            'email':forms.TextInput(attrs={'class':"form-control","id":"eemail","placeholder":"邮箱"}),
            'fox':forms.TextInput(attrs={'class':"form-control","id":"efox","placeholder":"传真"}),
            'url':forms.TextInput(attrs={'class':"form-control","id":"eurl","placeholder":"URL"}),
            'address':forms.TextInput(attrs={'class':"form-control","id":"eaddress","placeholder":"地址"}),
            'social_account':forms.TextInput(attrs={'class':"form-control","id":"esocial_account","placeholder":"社交帐号"}),
            'profile':forms.TextInput(attrs={'class':"form-control","id":"eprofile","placeholder":"输入内容"}),
            'custom':forms.TextInput(attrs={'class':"form-control","id":"ecustom","placeholder":"输入内容"}),
            'file_obj':forms.FileInput(attrs={"id":"file_obj","placeholder":"logo","name":"file_obj"}),
            'pic_head':forms.FileInput(attrs={"id":"pic_head","placeholder":"logo","name":"pic_head"}),
        }


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ('address_id','wechatid',)
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control width-70 pull-right","id":"name","placeholder":"姓名"}),
            'address':forms.TextInput(attrs={'class':"form-control width-70 pull-right","id":"address","placeholder":"收货地址"}),
            'phone':forms.TextInput(attrs={'class':"form-control width-70 pull-right","id":"phone","placeholder":"联系方式"}),
        }

