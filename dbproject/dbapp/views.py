from logging import exception
from django.shortcuts import render
from .models import Employee
# Create your views here.

def home(request):
    return render(request,'myhome.html')

def addemp(request):
    ResponseDic={}
    try:
        nm1=request.POST['nm']
        adrs=request.POST['adr']
        emplst=Employee(name=nm1,address=adrs)
        emplst.save()
        ResponseDic['msg']='Employee Added'
        return render(request,'myhome.html',ResponseDic)
    except Exception as e:
        print(e)
        ResponseDic['msg']='Employee not Added'
        return render(request,'myhome.html',ResponseDic)

def display(request):
    empdtls=Employee.objects.all()
    return render(request,'myhome.html',{'emp':empdtls})

def delete(request):
    try:
        Name=request.POST['nm2']
        empdtls=Employee.objects.filter(name=Name)
        empdtls.delete()
        return render(request,'myhome.html',{'key':'Deleted'})
    except Exception as e:
        print(e)
        return render(request,'myhome.html',{'key':'Not Deleted'})

def update(request):
    try:
        oldname=request.POST['oldname']
        newname=request.POST['newname']
        empdtls=Employee.objects.filter(name=oldname).update(name=newname)
        return render(request,'myhome.html',{'msg':'Updated'})
    except exception as e:
        print(e)
        return render(request,'myhome.html',{'msg':'Not Updated '})
