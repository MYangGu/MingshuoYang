from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!")
def about(request):
    return HttpResponse("Rango says here is about partner!"+'http://127.0.0.1:8000/rango/about/')

