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
        exclude = ('card_id',)