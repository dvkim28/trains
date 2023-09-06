from django.urls import path

from .views import AirplaneListView, AirplaneDetailView, AirplaneUpdateView

app_name = 'wagon'




urlpatterns = [
    path('', AirplaneListView.as_view(), name="homepage"),
    path('detail/<int:pk>/', AirplaneDetailView.as_view(), name="airplane_detail"),
    path('update/<int:pk>/', AirplaneUpdateView.as_view(), name="airplane_update"),
    # path('<slug:slug>/delete', CityDeleteView.as_view(), name="DeleteCity")
]
