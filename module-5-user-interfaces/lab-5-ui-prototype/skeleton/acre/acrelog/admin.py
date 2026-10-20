from django.contrib import admin

from .models import Field, Machine, Operation, Operator, Seed

admin.site.register(Operator)
admin.site.register(Field)
admin.site.register(Machine)
admin.site.register(Seed)
admin.site.register(Operation)
