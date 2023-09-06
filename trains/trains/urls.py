from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cities_main.urls')),
    path('airplane/', include('wagon.urls'))
]
