# Lecture 4.1 demo (2026). Field is the Farm tracker's Field from Lecture 3.3; Observation and its
# lookup list are from the 2024 farmnotes tutorial. Built and run on Django 5.2 LTS.
from django.db import models

FIELD_TYPES = [
    ('pasture', 'Pasture'),
    ('cropland', 'Cropland'),
]

OBSERVATION_TYPES = [
    ('weather', 'Weather'),
    ('crop', 'Crop'),
    ('soil', 'Soil'),
    ('water', 'Water'),
    ('pest', 'Pest'),
    ('other', 'Other'),
]

class Field(models.Model):
    name = models.CharField(max_length=200)
    acres = models.FloatField()
    field_type = models.CharField(choices=FIELD_TYPES, max_length=20)
    note = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.name} ({self.field_type}, {self.acres} acres)"

class Observation(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    observation_title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    observation_content = models.CharField(max_length=1000)
    observation_type = models.CharField(choices=OBSERVATION_TYPES, max_length=100)
    observation_date = models.DateField('date observed')

    def __str__(self):
        return f"{self.observation_title} by {self.author} on {self.observation_date}"
