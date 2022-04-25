from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Fish


def home(request):
    return HttpResponse('<h1>Hello World!</h1>')

def about(request):
  return render(request, 'about.html')

def fishes_index(request):
  fishes = Fish.objects.all()
  return render(request, 'fishes/index.html', { 'fishes': fishes })

def fishes_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  return render(request, 'fishes/detail.html', {'fish':fish})