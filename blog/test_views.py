from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class TestBlogListView(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="test_user", email="test@gmail.com",
            password="password123")

    def test_blog_list_view(self):
        resp = self.client.get(reverse('blog:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='blog/blog_list.html')
        self.assertTrue('blog_category_menu' in resp.context)
        self.assertTrue('blogs' in resp.context)

    def test_blog_create_view_logged_in_user(self):
        resp = self.client.get(reverse('blog:create'))
        self.assertEqual(resp.status_code, 302)

    def test_blog_create_view_abstract_user(self):
        resp = self.client.get(reverse('blog:create'))
        self.assertRedirects(resp, '/accounts/login/?next=/blog/create/')
        self.assertEqual(resp.status_code, 302)

    def test_blog_create_context_view(self):
        user = self.client.login(
            email="test@gmail.com", password="password123"
        )
        resp = self.client.get('/blog/create/')
        self.assertEqual(resp.context['view_type'], 'create')
        self.assertTemplateUsed(resp, template_name='blog/blog_form.html')
        self.assertEqual(resp.status_code, 200)

    def test_search_blog(self):
        resp = self.client.get(
            '/blog/search/?', {'q': 'Diet'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['search_term'], 'Diet')
        self.assertTemplateUsed(resp, template_name='blog/blog_search.html')
