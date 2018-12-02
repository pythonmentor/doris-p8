from django.test import TestCase

# Test signup
class RegisterTest(TestCase):

    def test_uses_signup_page(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
