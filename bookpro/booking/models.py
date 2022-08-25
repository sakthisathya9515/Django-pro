from ast import Return
from dataclasses import field
from multiprocessing.sharedctypes import Value
from unittest.util import _MAX_LENGTH
from click import Choice
from django.db import models
from django.forms import ChoiceField
from django.db.models import Sum

SUBSCRIB_CHOICE=(
    (1,'Subscription'),
    (2,'nonSubscription'))

SLOT=(
    (1,'08:00 PM(40)'), (2,'08:30 PM(40)'),
    (3,'09:00 PM(20)'), (4,'09:30 PM(20)'))    

ADDITIONAL=((1,'1'),(1,'2'),(1,'3'),(1,'4'),(1,'5')) 


# Create your models here.
class indexdb(models.Model):
    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Mobile_number =models.IntegerField(default=0)
    Department =models.CharField(max_length=255)


class primedb(models.Model):
    Subscription=models.IntegerField(choices=SUBSCRIB_CHOICE)


class subscribdb(models.Model):
    Subscriptionfee=models.IntegerField(default=2500)
    Contribution=models.IntegerField(default=0,blank=True)
    Additionalpass=models.IntegerField(default=0,choices=ADDITIONAL,blank=True)
    Slot_time=models.IntegerField(default=0,choices=SLOT,blank=True)
    payable=models.prefetch_related_objects
    
    class meta:
        db_table="subscrib"


    def payable(self):
        return self.Subscriptionfee+self.Contribution+self.Additionalpass*310
    
    

class nonsubscribdb(models.Model):
    Subscriptionfee=models.IntegerField(default=310)
    Contribution=models.IntegerField(default=0)
    Additionalpass=models.IntegerField(default=0,choices=ADDITIONAL,blank=True)
    Slot_time=models.IntegerField(default=0,choices=SLOT,blank=True)
    Payable=models.IntegerField(default=310)
        

        