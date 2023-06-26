from cProfile import label

from django import forms
from django.forms import TextInput
from .models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'slug']

        widgets = {
        "name": TextInput(attrs={
            'class':'form-control'
        }),
        "slug": TextInput(attrs={
            'class':'form-control'
        })
    }