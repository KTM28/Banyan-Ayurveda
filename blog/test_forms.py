from django.test import TestCase
from blog.forms import BlogForm, CommentForm
from blog.models import *

class TestBlogForm(TestCase):

    def test_blog_form_required(self):
        invalid_data = {
            'title': '',
            'category': '',
            'content': '',
            'thumbnail': '',
        }
        form = BlogForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('title', form.errors.keys())
        self.assertIn('category', form.errors.keys())
        self.assertIn('thumbnail', form.errors.keys())

class TestCommentForm(TestCase):

    def test_comment_form_required(self):
        form = CommentForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('content', form.errors.keys())
