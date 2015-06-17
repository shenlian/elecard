# Create your views here.
# coding=utf-8
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template import RequestContext

from home.models import ElectricCard
from home.form import ElectricCardForm
def index(request):

    # if request.method == "POST":
        

    data = {

    }
    return render(request,'home/electronic_edit.html',data) 

def finish(request):
    data = {

    }
    return render(request,'home/electronic_finish.html',data) 