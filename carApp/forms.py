from .models import CarModel
from django import forms

class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields= "__all__"

