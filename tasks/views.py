from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.

class AddTaskForm(forms.Form):
    task = forms.CharField(label="Add task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add_task(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]

            return HttpResponseRedirect(reverse("index"))
    else:
        form = AddTaskForm(request.POST)
        
        return render(request, "tasks/add.html", {
            "form": form
        })

    return render(request, "tasks/add.html", {
        "form": AddTaskForm()
    })