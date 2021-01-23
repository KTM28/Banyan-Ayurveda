from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestProfileView(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="test_user",
            email="test@gmail.com", password="password12345"
            )

    def test_user_profile_view_logged_in(self):
        user = self.client.login(
            email="test@gmail.com", password="password12345")
        resp = self.client.get(reverse('profile'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="profiles/profile.html")

    def test_user_profile_view_logged_out(self):
        resp = self.client.get(reverse('profile'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, "/accounts/login/?next=/profile/")

    def test_user_profile_logged_in_context(self):
        user = self.client.login(
            email="test@gmail.com", password="password12345")
        resp = self.client.get(reverse('profile'))
        self.assertTrue('user_blog' in resp.context)
        self.assertTrue('profile' in resp.context)
        self.assertTrue('orders' in resp.context)


class TestProfileDetailViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="test_user",
            email="test@gmail.com", password="password12345"
            )

    def test_Profile_shipping_view_logged_in(self):
        user = self.client.login(
            email="test@gmail.com", password="password12345")
        resp = self.client.get(reverse('shipping_info'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(
            resp, template_name="profiles/shipping_info.html")

    def test_Profile_shipping_view_logged_in_context(self):
        user = self.client.login(
            email="test@gmail.com", password="password12345")
        resp = self.client.get(reverse('shipping_info'))
        self.assertTrue('user' in resp.context)
