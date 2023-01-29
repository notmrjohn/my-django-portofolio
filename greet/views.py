from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Buna ziua!")

def greet(request, name):
    return render(request, "greet/index.html", {
        "name": name.capitalize()
    })