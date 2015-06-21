#coding=UTF-8
from home.models import *
from django.contrib import admin



#在admin中添加Poll模型
class Admin(admin.ModelAdmin):
    search_fields = ['telephone','userid__username']

RegisterClass=(ElectricCard,ShippingAddress,ExpressCompany)
for temp in RegisterClass:
    admin.site.register(temp, Admin)