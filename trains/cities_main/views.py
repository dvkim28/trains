from urllib import request

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .forms import CityForm
from .models import City


class TrainListView(ListView):
    model = City
    context_object_name = 'city'
    template_name = 'cities_main/index.html'

class CityCreateView(CreateView):
    model = City
    template_name = 'cities_main/includes/create_form.html'
    form_class = CityForm
    success_url = reverse_lazy('cities_main:homepage')

class CityUpdateView(UpdateView):
    model = City
    template_name = 'cities_main/update_city.html'
    success_url = reverse_lazy('cities_main:homepage')
    form_class = CityForm
