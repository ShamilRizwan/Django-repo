from logging import exception
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contacts

# Create your views here.
def home(request):
    return render(request,'myhome.html')




def addcont(request):
    ResponseDic={}
    try:
        nmbr=int(request.POST['num'])
        nam=request.POST['na']
        # phnnme=Contacts.objects.all().values_list('name')
        # phnnum=Contacts.objects.all().values_list('number')
        # phnlst=Contacts.objects.all()
        # if nam not in phnlst:
        #     if nmbr not in phnlst:
        #         phnlst=Contacts(name=nam,number=nmbr)
        #         phnlst.save()
        #         return render(request,'myhome.html',{'msg':'Contact Added'})
        # else:
        #     return render(request,'myhome.html',{'msg':'Already Exist'})

        if Contacts.objects.filter(name=nam).exists():
            ResponseDic['msg']='Already Exists'
            return render(request,'myhome.html',ResponseDic)
        else:
            phnlst=Contacts(name=nam,number=nmbr)
            phnlst.save()
            return render(request,'myhome.html',{'key':"Contact Added"})
    except exception as e:
        print(e)
        ResponseDic['msg']='Number Not Added'
        return render(request,'myhome.html',ResponseDic)


def display(request):
    phndtls=Contacts.objects.all()
    return render(request,'myhome.html',{'phn':phndtls})

def displayname(request):
    phnnme=Contacts.objects.all().values_list('name')
    return render(request,'myhome.html',{'phn':phnnme})


def delete(request):
    try:
        nmdlt=request.POST['nadel']
        phndtls=Contacts.objects.filter(name=nmdlt)
        phndtls.delete()
        return render(request,'myhome.html',{'key':'Deleted'})
    except exception as e:
        print(e)
        return render(request,'myhome.html',{'key':'Not Deleted'})


def update(request):
    try:
        oldname=request.POST['oldn']
        newname=request.POST['newn']
        phndtls=Contacts.objects.filter(name=oldname).update(name=newname)
        return render(request,'myhome.html',{'key':'Updated'})
    except exception as e:
        print(e)
        return render(request,'myhome.html',{'key':'Not Updated'})

