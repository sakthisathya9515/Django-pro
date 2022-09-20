from pickle import GET
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import Formindex, Formprime , Formsubscrib , Formnonsubscrib
from booking.models import SUBSCRIB_CHOICE ,SLOT
SUBSCRIB_CHOICE=(
    [1,'Sub'],
    [2,'nonSub'])

def index(request):
    form=Formindex
    if request.method=="POST":
        form=Formindex(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/prime')
    return render(request,'index.html',{'form':form})  

def prime(request):
    form=Formprime
    if request.method== 'POST':
        form=Formprime(request.POST)
    if request.choices==[1,'Sub']:
        return redirect (subscrib)
    return render( request,'prime.html',{'form':form},)      

def subscrib(request):
    form=Formsubscrib
    if request.method=="POST":
     form=Formsubscrib(request.POST)
     if form.is_valid():
        form.save()
        return redirect ('/subscribpay')
    return render( request,'subscrib.html',{'form':form},)


def nonsubscrib(request):
    form=Formnonsubscrib
    if request.method=="POST":
        form=Formnonsubscrib(request.POST)
    if form.is_valid():
        form.save()
        return redirect ('/nonsubscribpay')
    return render( request, 'nonsubscrib.html',{'form':form})

def subscribpay(request):
    return render(request,'subscribpay.html')

def nonsubscribpay(request):
    return render(request,'nonsubscribpay.html')    

    