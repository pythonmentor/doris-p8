from django.test import TestCase

class HomepageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'app/index.html')


    def test_uses_mentions_status_code(self):
            response = self.client.get('/mentions-legales/')
            self.assertEqual(response.status_code, 200)
