# Module 5 demo (2026), Lecture 5.4: unit tests. Run them with: python manage.py test
# Each test builds its own small database, so it never touches your real data.
from django.test import TestCase
from django.urls import reverse

from .models import Field, Observation


class FarmnotesTests(TestCase):

    # Runs before every test: one field to work with.
    def setUp(self):
        self.field = Field.objects.create(name='North 40', acres=40, field_type='cropland')

    # The home page lists my fields.
    def test_index_lists_fields(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'North 40')

    # A complete observation is saved, and the user is sent to that field's notes.
    def test_observe_saves_valid_observation(self):
        response = self.client.post(reverse('observe', args=[self.field.id]), {
            'observation_title': 'Aphids on soybeans',
            'author': 'Ankita',
            'observation_type': 'pest',
            'observation_date': '2026-10-29',
            'observation_content': 'Small colonies on the east edge.',
        })
        self.assertRedirects(response, reverse('notes', args=[self.field.id]))
        self.assertEqual(Observation.objects.count(), 1)

    # An incomplete observation is not saved, and the form says what's missing.
    def test_observe_rejects_missing_title(self):
        response = self.client.post(reverse('observe', args=[self.field.id]), {
            'author': 'Ankita',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        self.assertEqual(Observation.objects.count(), 0)
