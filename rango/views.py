from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!")

def about(request):
    return HttpResponse("Rango says here is about partner!"+'http://127.0.0.1:8000/rango/about/')

def about(request):
   return render(request, 'rango/about.html')

def index(request):

 context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
 return render(request, 'rango/index.html', context=context_dict)

