from django.db import models
from django.db.models import UniqueConstraint


class AnimalType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type} of breed {self.name}'


class Animal(models.Model):
    inventory_number = models.CharField(max_length=50, unique=True)
    is_male = models.BooleanField()
    name = models.CharField(max_length=50)
    arrival_date = models.DateField(auto_created=True)
    arrival_age_in_months = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey('Animal', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.breed.type} {self.name}'


class Weighting(models.Model):
    class Meta:
        constraints = [
            UniqueConstraint(fields=['animal', 'date'], name='one weighting per day')
        ]

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField()
    weight_kgs = models.FloatField()

    def __str__(self):
        return f'{self.date}: {self.animal} weights {self.weight_kgs} kgs'
