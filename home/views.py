# Create your views here.
# coding=utf-8
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template import RequestContext
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpResponseRedirect, HttpResponse
import hashlib, time, re
from xml.etree import ElementTree as ET

from home.models import ElectricCard,ShippingAddress,ExpressCompany
from home.form import *
from users.models import *
from home.utils import get_ecard_path
from const import CARD_STYLE_P1 , CARD_STYLE_P2

def edit(request,wechatid):
    print wechatid
    wechatid = WechatProfile.objects.get(wechatid = wechatid)
    express = ExpressCompany.objects.all()[0]
    if request.method == "POST":
        ele_obj = ElectricCard()
        ele_obj.wechatid = wechatid
        ele_obj.express = express
        # if request.FILES.has_key("pic_head"):
        #     f = request.FILES["pic_head"]
        #     pic = UploadedFile(f)
        #     ele_obj.pic_head = pic
        ele_obj.save()
        eleform = ElectricCardForm(request.POST,request.FILES,instance=ele_obj)
        if eleform.is_valid():
            name = ele_obj.name
            phone = ele_obj.phone
            email = ele_obj.email
            address = ele_obj.address
            url = ele_obj.url
            position = ele_obj.position
            eleform.save()
            path = get_ecard_path(name,phone,email,address,url,position,ele_obj.card_id)
            ele_obj.qrcode = "uploadfile/qrcode/%s.png" % ele_obj.card_id
            ele_obj.save()
            return HttpResponseRedirect('/finish/'+ ele_obj.card_id)
        else:
            print eleform.errors
    else:
        eleform = ElectricCardForm()

    data = {
        "eleform":eleform,
    }
    return render(request,'home/electronic_edit.html',data) 

def finish(request,card_id):
    ele_obj = ElectricCard.objects.get(card_id = card_id)
    data = {
        "ele_obj":ele_obj,
    }
    return render(request,'home/electronic_finish.html',data) 

def save_process(request):
    pass

# def login(request):
#     if request.method == "POST":
#         account = request.POST["account"]
#         we_pros = WechatProfile.objects.filter(wechatid = account)
#         if not we_pros:
#             wechat_obj = WechatProfile(wechatid = account)
#             wechat_obj.save()
#         else:
#             wechat_obj = we_pros[0]
#         return HttpResponseRedirect('edit/' + wechat_obj.wechatid)
#     data = {

#     }
#     return render(request,'home/login.html',data)   


def login(request):
    params = request.GET
    echostr = ""
    if params.has_key('echostr'):
        print "test echostr"
        echostr = request.GET['echostr']
        print echostr
        return HttpResponse(echostr)
    else:
        print "yidong"
        reply ="""<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[%s]]></Content>
        <FuncFlag>0</FuncFlag>
        </xml>"""
        if request.raw_post_data:
            print "youshuju"
            xml = ET.fromstring(request.raw_post_data)
            content = xml.find("Content").text
            fromUserName = xml.find("ToUserName").text
            toUserName = xml.find("FromUserName").text
            postTime = str(int(time.time()))
            print fromUserName
            print toUserName
            return HttpResponse(reply % (toUserName, fromUserName, postTime,"输入点命令吧..."))
        else:
            return HttpResponse("no reply") 

def cardstyle(request):
    ele_obj = ElectricCard.objects.all()[0]
    data = {
        "ele_obj":ele_obj,
        "CARD_STYLE_P1":CARD_STYLE_P1,
        "CARD_STYLE_P2":CARD_STYLE_P2,
    }
    return render(request,'home/card.html',data) 

def cardedit(request,cardstyle_id):
    ele_obj = ElectricCard.objects.all()[0]
    print cardstyle_id
    data = {
        "ele_obj":ele_obj,
        "cardstyle_id":cardstyle_id,
        "CARD_STYLE_P1":CARD_STYLE_P1,
        "CARD_STYLE_P2":CARD_STYLE_P2,
    }
    return render(request,'home/edit.html',data) 

def cardedit_after(request):
    print "cardedit_after"
    data = {

    }
    return render(request,'home/after_edit.html',data) 

def makeOrder(request):
    print "makeOrder"
    data = {

    }
    return render(request,'home/makeOrder.html',data) 


def shipaddress(request):
    address_list = ShippingAddress.objects.all()
    data = {
        "address_list":address_list,
    }
    return render(request,'home/shipAddress.html',data)

def enteraddress(request):
    addr_id = request.GET.get('p1',"")
    print addr_id
    wechatid = WechatProfile.objects.all()[0]
    if addr_id:
        print "youid"
        addr = ShippingAddress.objects.get(address_id=addr_id)
        if request.method == "POST":
            addr_form = ShippingAddressForm(request.POST,instance=addr)
            if addr_form.is_valid():
                addr_form.save()
                return HttpResponseRedirect('/shipaddress')
        else:
            addr_form = ShippingAddressForm(instance=addr)
    else:
        print "wudi"
        addr = ShippingAddress()
        addr.wechatid = wechatid
        addr.save()
        addr_form = ShippingAddressForm(instance=addr)
    data = {
        "addr_form":addr_form,
        "addr":addr,
    }
    return render(request,'home/enterAddress.html',data)

def confirmaddress(request,address_id):
    print address_id
    addr = ShippingAddress.objects.get(address_id=address_id)
    return HttpResponseRedirect('/makeOrder')

def shipway(request):
    data = {

    }
    return render(request,'home/shipway.html',data)


def electronic_edit(request):
    data = {

    }
    return render(request,'microbots/electronic_edit.html',data)

def card_holder(request):
    data = {

    }
    return render(request,'microbots/card_holder.html',data)

def electronic_finish(request):
    data = {

    }
    return render(request,'microbots/electronic_finish.html',data)