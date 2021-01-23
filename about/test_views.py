from django.test import TestCase


class TestView(TestCase):

    def test_get_about_page(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
