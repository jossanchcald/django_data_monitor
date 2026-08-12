from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'dashboard/base.html')

def index(request):
    data = {
        'title': "Landing Page' Dashboard",
    }

    return render(request, 'dashboard/index.html', data)