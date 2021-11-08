from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('view/', views.view, name="view"),
    path('create_form/', views.createPlant, name="create_form"),
    path('update_form/', views.updatePlant, name="update_form"),
]



