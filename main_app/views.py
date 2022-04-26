from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from .models import Fish
from .models import Toy


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


class FishCreate(CreateView):
    model = Fish
    fields = '__all__'

class FishUpdate(UpdateView):
  model = Fish
  # Let's disallow the renaming of a Fish by excluding the name field!
  fields = ['breed', 'description', 'age']

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fishes/'

class ToyIndex(TemplateView):
  template_name = 'toys/index.html'