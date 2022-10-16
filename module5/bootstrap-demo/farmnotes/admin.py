from django.contrib import admin

# Register your models here.
from .models import Field, Observation

admin.site.register(Field)
admin.site.register(Observation)