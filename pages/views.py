from django.shortcuts import render
from .models import Team

def home(request):
    teams = Team.objects.all() # fetch data from teams model
    data = {
        'teams' : teams,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')

def cars(request):
    return render(request, 'pages/cars.html')  

def services(request):
    return render(request, 'pages/services.html') 

def contact(request):
    return render(request, 'pages/contact.html') 
