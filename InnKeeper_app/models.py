from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_customer =models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(Login,on_delete=models.CASCADE,related_name='customer')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=500)
    def __str__(self):
        return self.name


class Owner(models.Model):
    user = models.OneToOneField(Login,on_delete=models.CASCADE,related_name='owner')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Resorts(models.Model):
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE,related_name='resort')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    # image
    picture =  models.FileField(upload_to='resorts/pictures/')
    pricing = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Facilities(models.Model):
    resort = models.ForeignKey(Resorts,on_delete=models.CASCADE,related_name='facilities')
    pool = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    lawn = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
