
from http.client import responses
from pyexpat import model
from random import choices
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import Formindex, Formprime , Formsubscrib , Formnonsubscrib
from booking.models import SUBSCRIB_CHOICE ,SLOT
SUBSCRIB_CHOICE=(
    (1,'Subscription'),
    (2,'nonSubscription'))

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
        if form.is_valid():
            form.save()
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

    