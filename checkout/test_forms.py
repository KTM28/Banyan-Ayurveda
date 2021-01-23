from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_order_form_valid_data(self):
        form = OrderForm(data={
            'full_name': 'test name',
            'email': 'test@gmail.com',
            'phone_number': '123456 789',
            'town_or_city': 'some city',
            'address_line1': '123 address street',
            'country': 'US'
        })
        self.assertTrue(form.is_valid())

    def test_OrderForm_invalid_data(self):
        form = OrderForm(data={
            'order_number': '',
            'user_profile': '',
            'full_name': '',
            'email': '',
            'phone_number': '',
            'address_line1': '',
            'address_line2': '',
            'town_or_city': '',
            'postcode': '',
            'county': '',
            'country': ''
        })
        self.assertFalse(form.is_valid())

    def test_order_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields,  (
            'full_name', 'email', 'phone_number',
            'address_line1', 'address_line2',
            'town_or_city', 'postcode', 'country',
            'county',))
