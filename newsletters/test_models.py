from django.test import TestCase
from newsletters.models import *

class TestNewslettersModels(TestCase):

    def test_user_email(self):
        MarketingSubs.objects.create(email='test@gmail.com')
        new_subscription = MarketingSubs.objects.get(id=1)
        self.assertEqual(new_subscription.email, 'test@gmail.com')