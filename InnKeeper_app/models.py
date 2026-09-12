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