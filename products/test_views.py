from django.test import TestCase
from django.urls import reverse
from products.views import *


class TestProduct(TestCase):

    fixtures = ['categories.json', 'products.json', ]

    def test_get_product(self):
        product = Product.objects.get(id=3)
        resp = self.client.get(reverse('products'))
        self.assertEqual(resp.status_code, 200)

    def test_get_product_contains(self):
        product = Product.objects.get(id=3)
        resp = self.client.get(reverse('products'))
        self.assertContains(resp, product.name)

    def test_product_search(self):
        resp = self.client.get(
            '/products/?', {'q': 'oils'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['search_term'], 'oils')
