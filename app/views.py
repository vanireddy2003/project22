from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hai(request,name):
    return HttpResponse(f'hello how are you {name}')