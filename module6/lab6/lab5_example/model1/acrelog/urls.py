from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_fields, name="index"),
    path("order_by/<str:order_by>/", views.get_fields_by_order, name="indexOrder"),
    path("<int:field_id>/", views.get_operations_by_field, name="field"),
]
