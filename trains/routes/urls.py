
from django.contrib import admin
from django.urls import path, include
from .views import home, find_route, add_route, save_route

urlpatterns = [
    path('', home, name='home'),
    path('find/', find_route, name='find_route'),
    path('add/', add_route, name='add_route'),
    path('save/', save_route, name='save_route'),

]
