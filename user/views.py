from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PlantsForm
from .filters import PlantFilter

# Create your views here.
from .models import *
from .scrape import *

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

##################################################################################################

def scrapeView(request):
    term = 'e'
    links = 'l'
    if request.method == "POST":
        term = request.POST["term"]

        # scrape(term)
        term = urllib.parse.quote_plus(term)
        response = get_source("https://pubmed.ncbi.nlm.nih.gov/?term=" + term)

        links = response.html.absolute_links

        record = Scrape(name=term,link=links)
        record.save()
        context = {'term':term}
        return render(request, 'accounts/success.html', context)
    context = {'term':term}
    return render(request, 'accounts/scrape.html',context)


import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

# from django.views.generic.list import ListView
#
# class Retrieve(ListView):

def retrieve(request):
    term = ''
    details = ''
    if request.method == "POST":
        term = request.POST["term"]

        details = Scrape.objects.all().filter(name__contains=term)

        context = {'term':term, 'details':details}

        return render(request, 'accounts/details.html', context)

    return render(request, 'accounts/retrieve.html')
