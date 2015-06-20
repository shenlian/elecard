#!/usr/bin/env python
# coding=utf-8
'''
 File Name: users/form.py
 Author: shenlian
 Created Time: 2014年05月30日 星期五 15时40分16秒
'''
from django import forms
from home.models import ElectricCard

class ElectricCardForm(forms.ModelForm):
    class Meta:
        model = ElectricCard
        exclude = ('card_id','uploadtime')
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control","id":"ename","placeholder":"姓名"}),
            'company':forms.TextInput(attrs={'class':"form-control","id":"ecompany","placeholder":"公司"}),
            'position':forms.TextInput(attrs={'class':"form-control","id":"eposition","placeholder":"职位"}),
            'phone':forms.TextInput(attrs={'class':"form-control","id":"ephone","placeholder":"电话"}),
            'email':forms.TextInput(attrs={'class':"form-control","id":"eemail","placeholder":"邮箱"}),
            'fox':forms.TextInput(attrs={'class':"form-control","id":"efox","placeholder":"传真"}),
            'url':forms.TextInput(attrs={'class':"form-control","id":"eurl","placeholder":"网址"}),
            'address':forms.TextInput(attrs={'class':"form-control","id":"eaddress","placeholder":"地址"}),
            'social_account':forms.TextInput(attrs={'class':"form-control","id":"esocial_account","placeholder":"社交帐号"}),
            'profile':forms.TextInput(attrs={'class':"form-control","id":"eprofile","placeholder":"个人简介"}),
            'custom':forms.TextInput(attrs={'class':"form-control","id":"ecustom","placeholder":"自定义"}),
            'file_obj':forms.FileInput(attrs={"id":"file_obj","placeholder":"logo","name":"file_obj"}),
        }
