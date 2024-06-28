from audioop import add
from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'myhome.html')
# def display(request):
#     return render(request,)
def display(request):
    a=int(request.POST['num1'])
    b=int(request.POST['num2'])
    c=request.POST['btn']
    if c=='+':
        d=a+b
    elif c=='-':
        d=a-b
    elif c=='*':
        d=a*b
    else:
        d=a/b
    return render(request,'myhome.html',{'key':d})

