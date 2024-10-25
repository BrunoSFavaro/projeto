from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     now = datetime.datetime.now()
#     return render(request, "newyear/index.html", {
#         "newyear": now.month == 1 and now.day == 1
#     })

def index(request):
    return render(request, "hello/index.html")

def bruno(request):
    return HttpResponse("Hello, Bruno!")

def alexandre(request):
    return HttpResponse("Hello, Alexandre!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
