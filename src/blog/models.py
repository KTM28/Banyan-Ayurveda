from django.db import models
from profiles.models import User

from ckeditor.fields import RichTextField


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name
        

class Blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=150)
    content = RichTextField(blank=True, null=True)
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
