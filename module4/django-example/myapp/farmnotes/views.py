from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Field, Observation


# Show all the fields in my farm
def index(request):
    latest_fields = Field.objects.all()
    context = {"latest_fields": latest_fields}
    return render(request, "farmnotes/index.html", context)


def notes(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    return render(request, "farmnotes/notes.html", {"field": field})


# View the details of a single observation
def observation(request, field_id, observation_id):
    observation = get_object_or_404(Observation, pk=observation_id)
    return render(request, "farmnotes/observation.html", {"observation": observation})
