# Module 5 demo (2026), Lecture 5.3: a form built from the Observation model.
from django import forms

from .models import Observation


class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        # The field this observation belongs to comes from the URL, so it isn't on the form.
        fields = ['observation_title', 'author', 'observation_type', 'observation_date', 'observation_content']

        # By default, Django will create default labels from the model field name
        # Django swaps underscore for spaces, and capitalizes the first letter
        # observation_title -> Observation title
        # Learn more here: https://docs.djangoproject.com/en/6.1/ref/forms/api/#ref-forms-api-outputting-html

        # You can add labels in the models.py - but this will apply to EVERY form, the admin portal etc.
        # You can insert labels here to override the default behaviors. If you skip something, it defaults to models.py 
        labels= {
            'observation_title': 'What do you observe?',
            'author': 'Who?',
            'observation_date': 'When?',
            'observation_content': 'Describe what you observed',
        }
    
        # widgets: give each input Bootstrap's class, and a date picker for the date.
        widgets = {
            'observation_title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'observation_type': forms.Select(attrs={'class': 'form-select'}),
            'observation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'observation_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
