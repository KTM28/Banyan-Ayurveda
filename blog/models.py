from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from profiles.models import User
from django.shortcuts import reverse

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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def get_like_url(self):
        return reverse('blog:like', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('blog:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('blog:delete', kwargs={'slug': self.slug})

    @property
    def comment(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

    @property
    def get_view_count(self):
        return self.blogview_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()


def create_slug(instance, new_slug=None):
    """Slugifys the title, if slug exists it adds a id to make it unique
    (Logic source:
    https://www.codingforentrepreneurs.com/blog/a-unique-slug-generator-for-django.)
    """

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    query_set = Blog.objects.filter(slug=slug)
    query_set_exists = query_set.exists()
    if query_set_exists:
        new_slug = str.format(slug, query_set.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def post_save_blog_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(post_save_blog_receiver, sender=Blog)


class Comment(models.Model):
    """function to Make comment on a blog post"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class BlogView(models.Model):
    """To Keep track of blog views."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):

    """To keep track of blog likes."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
