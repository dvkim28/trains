from django.urls import path

from .views import TrainListView

urlpatterns = [
    path('', TrainListView.as_view(), name="homepage")
]
