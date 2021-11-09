from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PlantsForm
from .filters import PlantFilter

# Create your views here.
from .models import *

def home(request):
    myFilter = PlantFilter()

    context = {'myFilter':myFilter}
    return render(request, 'accounts/dashboard.html', context)

def contact(request):
    return render(request, 'accounts/contact_us.html')

def about(request):
    return render(request, 'accounts/about_us.html')

def login(request):
    return render(request, 'accounts/login.html')

def view(request, pk_test):
    view = Plants.objects.all()
    plant = Plants.objects.get(id=pk_test)
    

    context = {'view':view, 'plant':plant}
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


def updatePlant(request, pk):
    plant = Plants.objects.get(id=pk)
    form = PlantsForm(instance=plant)

    if request.method == 'POST':
        form = PlantsForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}
    return render(request, 'accounts/plant_form.html', context)


def deletePlant(request, pk):
    plant = Plants.objects.get(id=pk)

    if request.method == "POST":
        plant.delete()
        return redirect('/')

    context = {'item':plant}
    return render(request, 'accounts/delete.html', context)



# def retrieve(request):
#     form = PlantsRetreive()

#     if request.method == 'GET':
#         form = PlantsRetreive(request.GET)

#     context = {'form':form}
#     return render(request, 'accounts/retrieve.html', context)
