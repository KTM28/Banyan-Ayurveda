from django.test import TestCase
from django.urls import reverse
from cart.views import add_to_cart, adjust_cart


class TestCartView(TestCase):

    fixtures = ['categories.json', 'products.json']

    def test_view_cart_view(self):
        resp = self.client.get(reverse('view_cart'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='cart/cart.html')

    def test_add_to_cart_view(self):
        resp = self.client.get(reverse('view_cart'))
        self.assertEqual(resp.status_code, 200)
