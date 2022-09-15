from django.shortcuts import render
from django.http import HttpResponse
from .models import Service

# Create your views here.

def services(request):
    services = Service.objects.all()
    return render(request, "services/services.html", {'services':services})