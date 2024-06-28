from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'myhome.html')

def display(request):
    num1=int(request.GET['txt1'])
    num2=int(request.GET['txt2'])
    num3=num1+num2
    return render(request,'myhome.html',{'key':num3})
# Create your views here.
