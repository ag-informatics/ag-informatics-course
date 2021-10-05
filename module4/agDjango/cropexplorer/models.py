from django.db import models

# Create your models here.


# Create your models here.
class Crop(models.Model):
    crop_name = models.CharField(max_length=50, default='')
    crop_scientific_name = models.CharField(max_length=50, default='')
    cover_crop_group = models.CharField(max_length=50, default='')
    family_common_name = models.CharField(max_length=50, default='')
    family_scientific_name = models.CharField(max_length=50, default='')
    zone_inclusion = models.CharField(max_length=50, default='')
    crop_description = models.CharField(max_length=500, default='')
    heat_tolerance = models.IntegerField(default=0)
    shade_tolerance = models.IntegerField(default=0)

    def __str__(self):
        return self.crop_name