from django.db import models


# Create your models here.
# Allow a user to sumbit the car's make, model, year, and mpg (miles per gallon).

class CarModel(models.Model):
    make = models.CharField(max_length=100, default="")
    model = models.CharField(max_length=100, default="")
    year = models.IntegerField(max_length=4, default=0)
    mpg = models.IntegerField()

    def __str__(self):
        return self.make, self.model
