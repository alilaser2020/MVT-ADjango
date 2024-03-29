from django.test import TestCase
from django.urls import reverse


class MessagePageTest(TestCase):
    def test_exist_url_at_correct_location(self):
        response = self.client.get('//')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('message'))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse('message'))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_content(self):
        response = self.client.get('//')
        self.assertContains(response, "<li>1th Hi, Django to DB</li>")
