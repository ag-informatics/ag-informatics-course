from django.db import models

# Create your models here.

OBSERVATION_TYPES = [
    ("weather", "Weather"),
    ("crop", "Crop"),
    ("soil", "Soil"),
    ("water", "Water"),
    ("pest", "Pest"),
    ("other", "Other"),
]

# class definitions below


class Field(models.Model):
    field_name = models.CharField(max_length=200)
    date_planted = models.DateTimeField("date planted")

    def __str__(self):
        return f"{self.field_name} planted on {self.date_planted.date()}"


class Observation(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    observation_title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    observation_content = models.CharField(max_length=1000)
    observation_type = models.CharField(choices=OBSERVATION_TYPES, max_length=100)
    observation_date = models.DateTimeField("date observed")

    def __str__(self):
        return f"{self.observation_title} by {self.author} on {self.observation_date.date()}"
