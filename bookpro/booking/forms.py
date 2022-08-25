from ast import Subscript
from dataclasses import field, fields
from importlib.metadata import files
from pickle import FALSE
from pyexpat import model
from random import choices
from urllib import request
from django import forms
from booking.models import indexdb, primedb,  subscribdb , nonsubscribdb
from booking.models import SUBSCRIB_CHOICE ,SLOT

class Formindex(forms.ModelForm):
    class Meta:
        model=indexdb
        fields=('First_name', 'Last_name', 'Email', 'Mobile_number' ,'Department')

class Formprime(forms.ModelForm):
    class Meta:
        model=primedb
        choices=SUBSCRIB_CHOICE
        fields=( 'Subscription',)
    


class Formsubscrib(forms.ModelForm):
    class Meta:
        model=subscribdb
        choices=SLOT
        fields=('Subscriptionfee','Contribution','Additionalpass','Slot_time','payable')
        

class Formnonsubscrib(forms.ModelForm):
    class Meta:
        model=nonsubscribdb
        choices=SLOT
        fields=('Subscriptionfee','Contribution','Additionalpass','Slot_time','Payable')  
        payable=forms.CharField
    

    
            