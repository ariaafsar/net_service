from django.db import models
from provider.models import Provider

class Product(models.Model) :
    name = models.CharField(max_length=50)
    price = models.FloatField()
    provider = models.ForeignKey(Provider , verbose_name=(""), on_delete=models.CASCADE , related_name="provider_name")
# Create your models here.
