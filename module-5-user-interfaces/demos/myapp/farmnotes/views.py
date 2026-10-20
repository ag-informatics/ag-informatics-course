from django.shortcuts import render, get_object_or_404, redirect

from .forms import ObservationForm
from .models import Field, Observation


# Show all the fields in my farm
def index(request):
    
    latest_fields = Field.objects.all()
    
    context = {'latest_fields': latest_fields}

    return render(request, 'farmnotes/index.html', context)


# List all notes related to a particular field
def notes(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    return render(request, 'farmnotes/notes.html', {'field': field})


# View the details of a single observation
def observation(request, field_id, observation_id):
    
    observation = get_object_or_404(Observation, pk=observation_id)

    return render(request, 'farmnotes/observation.html', {'observation': observation})


# Make an observation related to a particular field (Module 5: forms)
def observe(request, field_id):
    field = get_object_or_404(Field, pk=field_id)

    if request.method == 'POST':
        # The user submitted the form: fill it with what they sent, and check it.
        form = ObservationForm(request.POST)
        if form.is_valid():
            observation = form.save(commit=False)
            observation.field = field
            observation.save()
            return redirect('notes', field_id=field.id)
    else:
        # The user just arrived: show an empty form.
        form = ObservationForm()

    return render(request, 'farmnotes/observe.html', {'field': field, 'form': form})
