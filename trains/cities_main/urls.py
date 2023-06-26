from django.urls import path

from .views import TrainListView, CityCreateView, CityUpdateView
app_name = 'cities_main'

urlpatterns = [
    path('', TrainListView.as_view(), name="homepage"),
    path('create/', CityCreateView.as_view(), name="CreateCity"),
    path('update/<int:pk>', CityUpdateView.as_view(), name="UpdateCity")
]
