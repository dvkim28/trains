from django import forms
from django.forms import TextInput
from .models import Route
from cities_main.models import City


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(
        label='From city', queryset=City.objects.all(), widget = forms.Select(
            attrs={'class':'form-control js-example-basic-single'}
        )
    )
    to_city = forms.ModelChoiceField(
        label='To city', queryset=City.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control js-example-basic-single'}
        )
    )
    cities = forms.ModelMultipleChoiceField(
        label='Through cities', queryset=City.objects.all(), required=False, widget = forms.SelectMultiple(
            attrs={'class': 'form-control js-example-basic-multiple'}
        )
    )
    class Meta:
        model = Route
        fields = ['from_city', 'to_city', 'travel_times', 'trains']
        widgets = {
        "name": TextInput(attrs={
            'class':'form-control'
        }),
        "slug": TextInput(attrs={
            'class':'form-control'
        })
    }