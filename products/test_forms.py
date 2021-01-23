from django.test import TestCase
from .models import Product, Category
from .forms import ProductForm, ServiceForm


class TestProductForm(TestCase):

    def test_product_form_invalid_data(self):
        form = ProductForm(data={
            'name': 'test product',
            'description': 'test description',
            'sku': 'AT12345',
            'category': 'test category',
            'image_url': '',
            'image': '',
            'price': 5,
            'rating': 4.0,
            'discontinued': True,
        })
        self.assertFalse(form.is_valid())

    def test_product_form_metaclass(self):
        form = ProductForm()
        self.assertEqual(form.Meta.fields,  (
                    'name', 'description', 'sku',
                    'category', 'price',
                    'rating',
                    'image_url',
                    'image',
                    'discontinued',))


class TestServiceForm(TestCase):

    def test_service_form_invalid_data(self):
        form = ServiceForm(data={
            'name': 'test seervice',
            'description': '',
            'benefit': '',
            'duration': '',
            'image_url': '',
            'image': '',
            'price': '',
            'rating': ' ',
            'discontinued': '',
        })
        self.assertFalse(form.is_valid())

    def test_service_form_metaclass(self):
        form = ServiceForm()
        self.assertEqual(form.Meta.fields,  (
                    'name', 'description', 'benefit', 'price',
                    'rating', 'duration', 'image_url',
                    'image', 'discontinued',))
