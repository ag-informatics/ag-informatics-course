from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Field, Observation

# Create your views here.

#Show all the fields in my farm
def index(request):
    latest_fields = Field.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'farmnotes/index.html', context)

#List all notes related to a particular field
def notes(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    return render(request, 'farmnotes/notes.html', {'field': field})

#View the details of a single observation
def observation(request, field_id, observation_id):
	observation = get_object_or_404(Observation, pk=observation_id)
	return render(request, 'farmnotes/observation.html', {'observation': observation})

# #Version 1, STUBS
# #Show all the fields in my farm
# def index(request):
#     return HttpResponse("Hello, world! You're at the farmnotes index, or 'home' page.")

# #List all notes related to a particular field
# def notes(request, field_id):
#     return HttpResponse("You're looking at the notes related to field %s." % field_id)

# #View the details of a single observation
# def observation(request, field_id, observation_id):
#         return HttpResponse("You're looking at observation %s related to field %s." % (observation_id, field_id))

# #Make an observation related to a particular field
# def observe(request, field_id):
#     response = "This is where will will make an observation on field %s."
#     return HttpResponse(response % field_id)
# ```

