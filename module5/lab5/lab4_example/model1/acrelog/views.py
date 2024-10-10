from django.shortcuts import render, get_list_or_404
from .models import Field, Operation


# Create your views here.
def get_fields(request):
    fields = Field.objects.all()
    # You have a list of fields. You are in control and can process data here.
    fields = sorted(fields, key=lambda field: field.name)
    return render(request, "acrelog/index.html", {"fields": fields})


def get_operations_by_field(request, field_id):
    operations = get_list_or_404(Operation, location=field_id)
    operations = sorted(operations, key=lambda operation: operation.date, reverse=True)
    field = Field.objects.get(pk=field_id)
    return render(
        request, "acrelog/field.html", {"operations": operations, "field": field}
    )
