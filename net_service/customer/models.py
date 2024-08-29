from django.db import models

class Customer(models.Model) :
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    wallet = models.FloatField(default= 100_000)

# Create your models here.

