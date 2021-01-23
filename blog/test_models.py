from django.contrib.auth.models import User
from django.test import TestCase
from .models import Blog, BlogView, Like, Comment, Category

class TestCreateBlog(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="test_user", email="test@gmail.com", password="password1234"
        )

    def setUp(self):
        self.user = User.objects.get(username="test_user")

    def test_create_blog(self):
        new_blog = Blog.objects.create(
            title='test title',
            author=self.user,
            category="test Category",
            content="test content",
            slug="test_slug",
        )
        self.assertTrue(isinstance(new_blog, Blog))

class TestBlogDetail(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="test_user", email="test@gmail.com", password="password1234"
            )

    def setUp(self):
        self.user = User.objects.get(username="test_user")

        new_blog = Blog.objects.create(
            title='test title',
            author=self.user,
            category="test Category",
            content="test content",
            slug="test_slug",
        )
    
    def test_get_absolute_url(self):
        new_blog = Blog.objects.get(id=1)
        self.assertEquals(new_blog.get_absolute_url(), '/blog/test_slug/')
    
    def test_get_update_url(self):
        new_blog = Blog.objects.get(id=1)
        self.assertEquals(new_blog.get_absolute_url(), '/blog/test_slug/')

    def test_get_like_url(self):
        new_blog = Blog.objects.get(id=1)
        self.assertEquals(new_blog.get_absolute_url(), '/blog/test_slug/')

    def test_get_delete_url(self):
        new_blog = Blog.objects.get(id=1)
        self.assertEquals(new_blog.get_absolute_url(), '/blog/test_slug/')

    def test_get_category_url(self):
        new_blog = Blog.objects.get(id=1)
        self.assertTrue(new_blog.category, 'test Category')
