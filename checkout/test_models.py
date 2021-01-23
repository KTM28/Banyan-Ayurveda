from django.test import TestCase
from checkout.models import Order

class TestModelsCheckout(TestCase):

    @classmethod
    def setUpTestData(cls):
        Order.objects.create(
            order_number=2021,
            full_name="test_name",
            email="test@gmail.com",
            phone_number=123123456,
            country="GB",
            town_or_city="test city",
            address_line1="15 test street",
        )

    def test_checkout_details(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.full_name, "test_name")
        self.assertEqual(order.email, "test@gmail.com")
        self.assertEqual(order.country, "GB")
        self.assertEqual(order.town_or_city, "test city")

    def test_generate_order_number(self):
        order = Order.objects.get(id=1)
        self.assertFalse(order.order_number == 2021)