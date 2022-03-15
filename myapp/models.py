from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(unique=True,null=True)
    mobile = models.CharField(max_length=15,null=True)
    address = models.TextField(null=True)
    password = models.CharField(max_length=25,null=True)
    role = models.CharField(max_length=50,null=True)
    pic = models.FileField(upload_to='Profile Pic',default='avtar.png',null=True)

    def __str__(self):
        return self.email
        