from urllib import request

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .models import Airplane

from wagon.forms import AirplaneForm


class AirplaneListView(ListView):
    model = Airplane
    context_object_name = 'airplane'
    template_name = 'wagon/index.html'
    paginate_by = 5

class AirplaneDetailView(DeleteView):
    queryset = Airplane.objects.all()
    template_name = 'wagon/detail_view.html'

class AirplaneUpdateView(SuccessMessageMixin, UpdateView):
     model = Airplane
     template_name = 'wagon/update_airplane.html'
     form_class = AirplaneForm
     success_url = 'http://127.0.0.1:8000/'
     success_message = "Airplane was successfully updated"

# class CityUpdateView(SuccessMessageMixin, UpdateView):
#      model = Airplane
#      template_name = 'wagon/update_airplane.html'
#      success_url = 'http://127.0.0.1:8000/'
#      form_class = AirplaneForm
#      success_message = "Airplane was updated successfully"

# class CityDeleteView(SuccessMessageMixin, DeleteView):
#     model = City
#     template_name = 'cities_main/delete_city.html'
#     success_url = 'http://127.0.0.1:8000/'
#     success_message = "City was deleted successfully"

# Create your views here.
