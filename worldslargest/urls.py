
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('things/', include('worldslargestthings.urls')),
    path('admin/', admin.site.urls),
]
