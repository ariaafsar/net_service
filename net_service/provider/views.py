from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Provider
import json
@csrf_exempt
def provider_signup(request):
    if request.method == "POST" :
        body = json.loads(request.body)
        Provider.objects.create(
            name= body["name_inp"] , 
            email= body["email_inp"] , 
        )
        

    

# Create your views here.
