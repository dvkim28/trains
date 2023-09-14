
from django.contrib import admin
from django.urls import path, include
from .views import home, find_route, add_route

urlpatterns = [
    path('',home, name='home'),
    path('find/',find_route, name='find_route'),
    path('add/',add_route, name='add_route'),

]
