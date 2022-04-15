from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=25,null=True)
    address = models.TextField(null= True)
    doj = models.DateField(null=True)
    pic = models.FileField(upload_to='Profile Pic',default='avtar.png',null=True)

    def __str__(self):
        return self.name + '------' + self.email


class Category(models.Model):
    category = models.CharField(max_length=25)

    def __str__(self):
        return self.category

class Product(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    name =  models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    size = models.IntegerField()
    price = models.IntegerField()
    des = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    pic = models.FileField(upload_to='shoesimg',default='avtar.png',null=True)

    def __str__(self):
        return self.seller.name + ' >>>> ' + self.name    
