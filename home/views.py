# Create your views here.
# coding=utf-8
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template import RequestContext
from django.core.files.uploadedfile import UploadedFile

from home.models import ElectricCard
from home.form import ElectricCardForm
def index(request):
    print "hahhahahdsa"
    if request.method == "POST":
        eleform = ElectricCardForm(request.POST,request.FILES)
        if eleform.is_valid():
            name = eleform.cleaned_data["name"]
            files = eleform.cleaned_data["file_obj"]
            eleform.save()
            # f = request.FILES["file_obj"]
            # wrapper_f = UploadedFile(f)
            # ele_obj = eleform.save(commit=false)
            # ele_obj.file_obj = wrapper_f
            # ele_obj.save()
            print name
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