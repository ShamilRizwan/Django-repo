from http.client import HTTPResponse
from logging import exception
from django.shortcuts import render
from django.http import HttpResponse
from .models import ExpenseT
from .models import Balance
# Create your views here.

def home(request):
    return render(request,'index.html')

def bale(request):
    ResponseDic={}
    try:
        balance=int(request.POST['bal'])
        balencelst=Balance(balamt=balance)
        balencelst.save()
        ResponseDic['msg']='Balance Added'
        return render(request,'index.html',ResponseDic)
    except exception as e:
        print(e)
        ResponseDic['msg']='Number Not Added'
        return render(request,'index.html',ResponseDic)

       


def delete(request):
    try:
        expdlt=request.POST['expdel']
        expdtls=ExpenseT.objects.all()
        expdtls=ExpenseT.objects.filter(expname=expdlt)
        expdtls.delete()
        return render(request,'index.html',{'key':'Deleted'})
    except exception as e:
        print(e)
        return render(request,'index.html',{'key':'Not Deleted'})


def addexp(request):
    ResponseDic={}
    try:
        expp=request.POST['expnme']
        amtt=request.POST['expamt']
        mylst=Balance.objects.filter(id=12)
        for i in mylst:
            bal=i.balamt
        if amtt>bal:
            ResponseDic['msg']='Insufficient Balance'
            return render(request,'index.html',ResponseDic)
        else:
            bal=bal-amtt
            mylst=Balance.objects.all().update(balance=bal)

        mylstt=ExpenseT.objects.all()
        for i in mylstt:
            if i in mylstt:
                if expp in i.expname:
                    flag=0
                    amtt=i.expense
                else:
                    flag=1

            if flag==0:
                Amt=amtt+Amt
                ExpenseT.objects.filter(expname=expp).update(expense=Amt)
            elif flag==1:
                mylst=ExpenseT(expname=expp,expense=Amt)
                mylst.save()

            ResponseDic['key']='Expense Added'
            return render(request,'index.html',ResponseDic)
    except exception as e:
        print(e)
        ResponseDic['key']='Expense Not Added'
        return render(request,'index.html',ResponseDic)
        
