from django.db import models
from django.urls import reverse
from datetime import date

class Rod(models.Model):
  name = models.CharField(max_length=50)
  typeOfRod = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('rods_detail', kwargs={'pk': self.id})


# Create your models here.
class Fish(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    rods = models.ManyToManyField(Rod, blank=True)

    def __str__(self):
        return f"The fish named {self.name} has an id of {self.id}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'fish_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        #choices
        choices= MEALS,
        default=MEALS[0][0]
    )

    #  the foreign key always goes on the many side
    #internally it will be cat_id the _id automatically gets added
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

    def __str__(self):
        #this method will give us friendly field choices value (breakfast instead of B)
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering: ['-date']