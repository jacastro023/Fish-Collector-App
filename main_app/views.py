from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Fish:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

fishes = [
  Fish('Lolo', 'tabby', 'foul little demon', 3),
  Fish('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Fish('Raven', 'black tripod', '3 legged cat', 4)
]


def home(request):
    return HttpResponse('<h1>Hello World!</h1>')

def about(request):
  return render(request, 'about.html')

def fishes_index(request):
  return render(request, 'fishes/index.html', { 'fishes': fishes })