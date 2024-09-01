from django.shortcuts import render
from django.http import HttpResponse #importante para definir las rutas


# Create your views here.
def helloworld(request):
    return HttpResponse('Hello world')