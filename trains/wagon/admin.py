from django.contrib import admin

from wagon.models import Airplane


class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
admin.site.register(Airplane, AirplaneAdmin)