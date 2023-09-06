from django.contrib import admin
from .models import Airplane

class AirplaneAdmin(admin.ModelAdmin):
        list_display = ('id', 'name', 'from_city', 'to_city', 'travel_time')
        list_editable = ('name', 'travel_time')
admin.site.register(Airplane, AirplaneAdmin)