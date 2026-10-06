from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('farmnotes/', include('farmnotes.urls')),
    path('admin/', admin.site.urls),
]
