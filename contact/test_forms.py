from django.test import TestCase
from contact.forms import ContactForm


class TestContacForm(TestCase):

    def test_contact_form_valid(self):

        form = ContactForm({'full_name': 'test name',
                            'email': 'test@test.com',
                            'message': 'test message',
                            })
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid(self):

        form = ContactForm({'full_name': 'test name',
                            'email': 'test',
                            'message': 'test message',
                            })
        self.assertFalse(form.is_valid())
