from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse('Welcome to Django')
    return render(request,'myhome.html')

def display(request):
    myname=request.GET['txt1']
    return render(request,'myhome.html',{'key':'welcome '+myname})