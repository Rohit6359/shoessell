


from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=25)
    pic=models.FileField(upload_to='Profile Pic',default='avtar.png')


    def __str__(self):
        return self.email