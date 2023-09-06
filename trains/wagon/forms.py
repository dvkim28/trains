from cProfile import label

from django import forms
from django.forms import TextInput
from .models import Airplane
from cities_main.models import City


class AirplaneForm(forms.ModelForm):
        name = forms.CharField(label="Airplane", widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Airplane'
        }))
        travel_time = forms.IntegerField(label="Time in road",
                                         widget=forms.NumberInput(attrs={
                                             'class':'form-control',
                                             'placeholder': 'Travel time'
                                         }
        ))
        from_city = forms.ModelChoiceField(
            label="From city", queryset=City.objects.all(), widget = forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder': 'From city'
                       }
            ))
        to_city = forms.ModelChoiceField(
            label="To city", queryset=City.objects.all(), widget = forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder': 'To city'
                       }
            ))

        class Meta:
            model = Airplane
            fields = '__all__'