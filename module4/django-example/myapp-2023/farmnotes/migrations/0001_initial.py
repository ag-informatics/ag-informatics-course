# Generated by Django 5.1.1 on 2024-09-29 02:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=200)),
                ('date_planted', models.DateTimeField(verbose_name='date planted')),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation_title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('observation_content', models.CharField(max_length=1000)),
                ('observation_type', models.CharField(choices=[('weather', 'Weather'), ('crop', 'Crop'), ('soil', 'Soil'), ('water', 'Water'), ('pest', 'Pest'), ('other', 'Other')], max_length=100)),
                ('observation_date', models.DateTimeField(verbose_name='date observed')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmnotes.field')),
            ],
        ),
    ]
