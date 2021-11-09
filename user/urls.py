from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('view/<str:pk_test>/', views.view, name="view"),
    path('create_form/', views.createPlant, name="create_form"),
    path('update_form/<str:pk>/', views.updatePlant, name="update_form"),
    path('delete_form/<str:pk>/', views.deletePlant, name="delete_form"),
]



