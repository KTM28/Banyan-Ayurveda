from django.test import TestCase
from django.urls import reverse


class TestContactView(TestCase):

    def test_contact_view(self):
        resp = self.client.get(reverse('contact'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='contact/contact.html')

    def test_contact_success_view(self):
        resp = self.client.get(reverse('contact_success'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(
            resp, template_name='contact/contact_success.html'
            )
