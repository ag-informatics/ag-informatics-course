# Generated by Django 3.2.7 on 2021-09-19 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmnotes', '0005_alter_observation_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='photo',
            field=models.FileField(upload_to='farmnotes/uploads/'),
        ),
    ]
