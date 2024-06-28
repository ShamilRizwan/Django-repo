from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'myhome.html')
def display(request):
    num1=int(request.POST['mrk1'])
    num2=int(request.POST['mrk2'])
    num3=int(request.POST['mrk3'])
    gr=(num1+num2+num3)/3
    if gr>=90:
        return render(request,'second.html',{'key':'A'})
    elif gr>=80:
        return render(request,'second.html',{'key':'B'})
    elif gr>=70:
        return render(request,'second.html',{'key':'C'})
    elif gr>=60:
        return render(request,'second.html',{'key':'D'})
    else:
        return render(request,'second.html',{'key':'FAILED'})


