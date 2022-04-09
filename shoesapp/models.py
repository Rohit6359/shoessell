from django.db import models

# Create your models here.

class Client(models.Model) :
    fname = models.CharField(max_length=50,null=True)
    lname = models.CharField(max_length=50,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=25,null=True)
    address = models.TextField(null= True)
    pic = models.FileField(upload_to='Profile Pic',default='avtar.png',null=True)

    def __str__(self):
        return self.Fname + '------' + self.email