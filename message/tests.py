from django.test import SimpleTestCase


class MessagePageTest(SimpleTestCase):
    def test_exist_url_at_correct_location(self):
        response = self.client.get('/message/')
        self.assertEqual(response.status_code, 200)
