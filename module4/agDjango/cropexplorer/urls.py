from django.urls import path

from . import views

urlpatterns = [
    
    # URL example: /crops/
    path('', views.index, name='index'),

]