from django.shortcuts import render, get_list_or_404
from .models import Field, Operation


# Create your views here.
def get_fields(request):
    fields = Field.objects.all()
    operations = [
        Operation.objects.filter(location=field).order_by("-date").first()
        for field in fields
    ]
    return render(request, "index.html", {"operations": operations})

def get_fields_by_order(request, order_by):
    fields = Field.objects.all()
    operations = [
        Operation.objects.filter(location=field).order_by("-date").first()
        for field in fields
    ]
    match  order_by:
        case "time":
            operations = sorted(operations, key=lambda operation: operation.date, reverse=True)
        case "name":
            operations =sorted(operations, key=lambda operation: operation.location.name)
    
    return render(request, "index.html", {"operations": operations})


def get_operations_by_field(request, field_id):
    operations = get_list_or_404(Operation, location=field_id)
    operations = sorted(operations, key=lambda operation: operation.date, reverse=True)
    field = Field.objects.get(pk=field_id)
    return render(
        request, "field.html", {"operations": operations, "field": field}
    )
