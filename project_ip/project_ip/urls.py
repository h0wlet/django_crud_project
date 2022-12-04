from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('app_ip/', include('app_ip.urls')),
    path('admin/', admin.site.urls)
]

