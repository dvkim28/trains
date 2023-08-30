from django.urls import path

from .views import TrainListView, CityCreateView, CityUpdateView, CityDeleteView

app_name = 'cities_main'

urlpatterns = [
    path('', TrainListView.as_view(), name="homepage"),
    path('create/', CityCreateView.as_view(), name="CreateCity"),
    path('update/<slug:slug>', CityUpdateView.as_view(), name="UpdateCity"),
    path('<slug:slug>/delete', CityDeleteView.as_view(), name="DeleteCity")
]
