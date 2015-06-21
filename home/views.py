# Create your views here.
# coding=utf-8
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template import RequestContext
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpResponseRedirect, HttpResponse
import hashlib, time, re
from xml.etree import ElementTree as ET

from home.models import ElectricCard
from home.form import ElectricCardForm
from users.models import *
def index(request):
    wechatid = WechatProfile.objects.all()[0]
    if request.method == "POST":
        eleform = ElectricCardForm(request.POST,request.FILES)
        if eleform.is_valid():
            #name = eleform.cleaned_data["name"]
            #files = eleform.cleaned_data["file_obj"]
            elinfo = eleform.save(commit = False)
            elinfo.wechatid = wechatid
            elinfo.save()
            return HttpResponseRedirect('finish')
        else:
            print eleform.errors
    else:
        eleform = ElectricCardForm()

    data = {
        "eleform":eleform,
    }
    return render(request,'home/electronic_edit.html',data) 

def finish(request):
    data = {

    }
    return render(request,'home/electronic_finish.html',data) 

def save_process(request):
    pass

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