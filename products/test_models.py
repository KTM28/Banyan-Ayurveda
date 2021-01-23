from django.test import TestCase
from .models import Product


class ProductModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name="test_product",
            description="test descriptions",
            price=5,
        )

    def test_product_name(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.name, "test_product")

    def test_product_description(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.description, "test descriptions")

    def test_product_is_a_treatment(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.is_a_treatment, False)

    def test_product_discontinued(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.discontinued, False)