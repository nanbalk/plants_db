from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PlantsForm

# Create your views here.
from .models import *

def home(request):
    return render(request, 'accounts/dashboard.html')

def contact(request):
    return render(request, 'accounts/contact_us.html')

def about(request):
    return render(request, 'accounts/about_us.html')

def login(request):
    return render(request, 'accounts/login.html')

def view(request):
    # view = Plants.objects.get(id=pk_test)
    view = Plants.objects.all()

    context = {'view':view,}
    return render(request, 'accounts/view.html', context)

def createPlant(request):

    form = PlantsForm()
    if request.method == 'POST':
        form = PlantsForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/plant_form.html', context)


def updatePlant(request):

    # plant = Plants.objects.get(id=pk)
    form = PlantsForm()

    if request.method == 'POST':
        form = PlantsForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/plant_form.html', context)

# def retrieve(request):
#     form = PlantsRetreive()

#     if request.method == 'GET':
#         form = PlantsRetreive(request.GET)

#     context = {'form':form}
#     return render(request, 'accounts/retrieve.html', context)
