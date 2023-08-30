from urllib import request

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .forms import CityForm
from .models import City


class TrainListView(ListView):
    model = City
    ordering = 'created'
    context_object_name = 'city'
    template_name = 'cities_main/index.html'

class CityCreateView(CreateView):
    model = City
    template_name = 'cities_main/includes/create_form.html'
    form_class = CityForm
    success_url = 'http://127.0.0.1:8000/'
class CityUpdateView(UpdateView):
    model = City
    template_name = 'cities_main/update_city.html'
    success_url = 'http://127.0.0.1:8000/'
    form_class = CityForm
class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities_main/delete_city.html'
    success_url = 'http://127.0.0.1:8000/'