from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
Inicio home/
Historia about/
Servicios services/
Visitanos store/
Contacto contact/
Blog blog/
Sample sample/
"""

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def store(request):
    return render(request, "core/store.html")
