from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from .models import Fish
from .models import Toy
from .forms import FeedingForm


def home(request):
    return HttpResponse('<h1>Hello World!</h1>')

def about(request):
  return render(request, 'about.html')

def fishes_index(request):
  fishes = Fish.objects.all()
  return render(request, 'fishes/index.html', { 'fishes': fishes })

def fishes_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  feeding_form = FeedingForm()
  return render(request, 'fishes/detail.html', {'fish':fish, 'feeding_form':feeding_form})


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

def add_feeding(request, fish_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the fish_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('detail', fish_id=fish_id)