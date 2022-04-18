
from datetime import date
from pickle import TRUE
from pyexpat import model
from time import time
from django.db import models

from myapp.models import Product

# Create your models here.

class Client(models.Model):
    fname = models.CharField(max_length=50,null=True)
    lname = models.CharField(max_length=50,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=25,null=True)
    address = models.TextField(null= True)
    pic = models.FileField(upload_to='Profile Pic',default='avtar.png',null=True)

    def __str__(self):
        return self.fname + '------' + self.email

class Booking(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    address = models.TextField()
    pay_mode = models.CharField(max_length=50,choices=[('COD','COD'),('Online','Online')])
    pay_id = models.CharField(max_length=30,null=True,blank=True)
    verify = models.BooleanField(default=False)
    amount = models.IntegerField(default=0)
    pay_at = models.DateTimeField(auto_now_add =True)
    
    def __str__(self):
        return str(self.product.name)

