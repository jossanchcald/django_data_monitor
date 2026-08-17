from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'dashboard/base.html')

@login_required
def index(request):

    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON

    # Número total de respuestas
    total_responses = len(posts)

    listaDatos = list(posts.values())

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
        'responses': listaDatos[:10],
    }

    return render(request, 'dashboard/index.html', data)