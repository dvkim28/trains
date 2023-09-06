from django.urls import path

from .views import AirplaneListView, AirplaneDetailView, AirplaneUpdateView, AirplaneDeleteView, AirplaneCreateView

app_name = 'wagon'




urlpatterns = [
    path('', AirplaneListView.as_view(), name="homepage"),
    path('detail/<int:pk>/', AirplaneDetailView.as_view(), name="airplane_detail"),
    path('update/<int:pk>/', AirplaneUpdateView.as_view(), name="airplane_update"),
    path('delete/<int:pk>/', AirplaneDeleteView.as_view(), name="DeleteAirplane"),
    path('create/', AirplaneCreateView.as_view(), name="CreateAirplane"),
]
