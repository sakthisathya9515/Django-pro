from http.client import OK
from operator import is_not
from pickle import GET
from pyexpat import model
from random import choices
from secrets import choice
from subprocess import check_output
from tabnanny import check
from bson import is_valid
from django.forms import ChoiceField
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from matplotlib.pyplot import get
from matplotlib.style import context
from numpy import choose
from .forms import Formindex, Formprime , Formsubscrib , Formnonsubscrib
from booking.models import SUBSCRIB_CHOICE ,SLOT, primedb

def index(request):
    form=Formindex
    if request.method=="POST":
        form=Formindex(request.POST )
        if form.is_valid():
            form.save()
            return redirect('/prime')
    return render(request,'index.html',{'form':form})  

def prime(request):
    form=Formprime
    if request.method=="POST":
        form=Formprime(request.POST)
        if form.is_valid():
           form.save()
           pass            
        if SUBSCRIB_CHOICE==(1):
               return redirect('/subscrib')
        else:
               return redirect('/nonsubscrib')
    return render(request,'prime.html',{'form':form})
    

def subscrib(request):
    form=Formsubscrib
    if request.method=="POST":
        form=Formsubscrib(request.POST)
        if form.is_valid():
            form.save() 
    return render( request,'subscrib.html',{'form':form})

def nonsubscrib(request):
    form=Formnonsubscrib
    if request.method=="POST":
        form=Formnonsubscrib(request.POST)
        if form.is_valid():
            form.save()
    return render( request, 'nonsubscrib.html',{'form':form})


    