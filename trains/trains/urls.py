
from django.contrib import admin
from django.urls import path, include
from routes.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cities_main.urls')),
    path('airplane/', include('wagon.urls')),
    path('route/', include('routes.urls') )
]
