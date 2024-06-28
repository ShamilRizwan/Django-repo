from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'myhome.html')
# Create your views here.
def display(request):
    age=int(request.POST['txt1'])
    if(age>=18):
        return render(request,'second.html',{'key':'You are eligible'})
    else:
        return render(request,'second.html',{'key':"You are not eligible"})