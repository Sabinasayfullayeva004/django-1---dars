from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello_world(requist):
    return HttpResponse("<h1>Assalomu alaykum Sifat</h1>")