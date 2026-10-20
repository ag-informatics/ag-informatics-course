from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_fields, name="index"),
    path("<int:field_id>/", views.get_operations_by_field, name="field"),
]
