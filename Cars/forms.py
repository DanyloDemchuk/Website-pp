from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["owner", "plate", 'car_name', 'max_speed']


class CarEdit(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"