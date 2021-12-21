from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def first_index(request):
    return HttpResponse('<h1>Hello, world!!!</h1>')