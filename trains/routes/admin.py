from django.contrib import admin
from .models import Route


class RouteAdmin(admin.ModelAdmin):
        list_display = ('id', 'name', 'from_city', 'travel_times')
admin.site.register(Route, RouteAdmin)