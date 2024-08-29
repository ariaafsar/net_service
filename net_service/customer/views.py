from django.shortcuts import render
import json
from .models import Customer  
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from product.models import Product 
from provider.models import Sale




@csrf_exempt
def signup(request):
    if request.method == "POST" :
        body = json.loads(request.body)
        Customer.objects.create(
            name = body['naem_inp'] ,
            email = body['email_inp'] , 
        )
        return HttpResponse("new customer added")
    else :
        return HttpResponse("badrequest")
    
def make_sale(request):
    if request.method == "POST" :
        body = json.loads(request.body)
        product_lst = Product.objects.all()
        lst = []
        for i in product_lst :
            lst.append(i)
        selcted_prod = Product.objects.get(id=body['prod_inp'])
        Sale.objects.create(
            
        )


# Create your views here.
