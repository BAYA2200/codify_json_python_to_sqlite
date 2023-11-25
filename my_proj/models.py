from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()

class Work(models.Model):
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    postalZip = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Account(models.Model):
    pin = models.IntegerField()
    acc_num = models.CharField(max_length=30)
    pan = models.CharField(max_length=30)
    cvv = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)