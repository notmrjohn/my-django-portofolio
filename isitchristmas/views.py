import datetime
from django.shortcuts import render, HttpResponse

# Create your views here.

def is_it_christmas(request):
    today = datetime.datetime.now()
    return render(request, "isitchristmas/index.html", {
        "christmas": today.month == 12 and today.day == 25
    })