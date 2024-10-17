from django.shortcuts import render
from proba.models import Patients


# Create your views here.

def index(request):
    context = {}
    score1 = Patients.objects.all()
    context['score1'] = score1

    context['title'] = 'Home'
    return render(request, 'index.html', context)

def about(request):
    context = {}
    context['title'] = 'About'
    return render(request, 'about.html', context)