from django.contrib import admin

from .models import Blog, BlogView, Comment, Like, Category


class BlogListAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',
                    'category',)
    list_filter = ('author', 'category',)


admin.site.register(Blog, BlogListAdmin)
admin.site.register(BlogView)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Like)
