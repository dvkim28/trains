from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'created')
admin.site.register(City, CityAdmin)