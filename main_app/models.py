from django.db import models
from django.urls import reverse
# Create your models here.
class Fish(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"The fish named {self.name} has an id of {self.id}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'fish_id': self.id})


class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
        return f"The toy named {self.name} has a color of {self.color} and an id of {self.id}"