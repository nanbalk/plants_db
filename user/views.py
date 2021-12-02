from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from .forms import PlantsForm
from .filters import PlantFilter

# Create your views here.
from .models import *
from .scrape import *

def home(request):
    if request.method == "POST":
        try:
            search_term = request.POST.get("search")
            plant_view = Plants.objects.get(name=search_term)
        except Exception as e:
            raise e

        context = {'search_term':search_term, 'plant_view':plant_view}

        return render(request, 'accounts/plant_view.html', context)

    # myFilter = PlantFilter()
    #
    # context = {'myFilter':myFilter}
    return render(request, 'accounts/dashboard.html')


def contact(request):
    return render(request, 'accounts/contact_us.html')

def about(request):
    return render(request, 'accounts/about_us.html')



def view(request,pk_test):
    view = Plants.objects.all()
    plant = Plants.objects.get(id=pk_test)


    context = {'view':view, 'plant':plant}
    return render(request, 'accounts/view.html', context)
@login_required
def createPlant(request):

    form = PlantsForm()
    if request.method == 'POST':
        form = PlantsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/plant_form.html', context)

@login_required
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

@login_required
def deletePlant(request, pk):
    plant = Plants.objects.get(id=pk)

    if request.method == "POST":
        plant.delete()
        return redirect('/')

    context = {'item':plant}
    return render(request, 'accounts/delete.html', context)

##################################################################################################
@login_required
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
@login_required
def retrieve(request):
    term = ''
    details = ''
    if request.method == "POST":
        term = request.POST.get("term")

        details = Scrape.objects.get(name=term)

        context = {'term':term, 'details':details}

        return render(request, 'accounts/details.html', context)

    return render(request, 'accounts/retrieve.html')


####################################################################################################################


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
