from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CarModel
from .forms import CarForm


# Create your views here.

def cars(request):
    allCars = CarModel.objects.all()
    carform = CarForm()
    context = {
        "carform": carform,
        "allCars" : allCars,
    }

    return render(request, "carApp/carEntries.html", context)


def congrats(request):
    return render(request, "carApp/congrats.html")
