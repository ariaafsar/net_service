from django.db import models
from product.models import Product

class Provider(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="producrt_name")
    active = models.BooleanField(default= False)
# Create your models here.
class Sale(models.Model):
    customer_name =models.CharField(max_length=50)
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name= "sale_product_name")