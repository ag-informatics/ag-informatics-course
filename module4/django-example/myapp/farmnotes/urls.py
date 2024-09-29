from django.urls import path

from . import views

urlpatterns = [
    # /farmnotes
    path("", views.index, name="index"),
    # /farmnotes/field_id
    # /farmnotes/5/
    path("<int:field_id>/", views.notes, name="notes"),
    # farmnotes/field_id/observation_id/
    # 3rd observation for my 4th field
    # farmnotes/4/3/
    path("<int:field_id>/<int:observation_id>/", views.observation, name="observation"),
]
