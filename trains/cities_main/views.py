from urllib import request

from django.shortcuts import render
from django.views.generic import ListView

from .models import City


class TrainListView(ListView):
    model = City
    paginate_by = 5
    context_object_name = 'city'
    template_name = 'cities_main/index.html'
