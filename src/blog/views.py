from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog, BlogView, Like, Comment, Category
from .forms import BlogForm


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    ordering = ['-publish_date']
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        blog_category_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['blog_category_menu'] = blog_category_menu
        return context

def CategoryView(request, category):
    blog_category = Blog.objects.filter(category=category)
    blog_category_menu = Category.objects.all()
    blogs = Blog.objects.all()
    context = {
        'category': category,
        'blog_category': blog_category,
        'blog_category_menu': blog_category_menu,
        'blogs': blogs
    }
    return render(request, 'blog/blog_categories.html', context)

class BlogDetailView(DetailView):
    model = Blog
    
    def post(self, *args, **kwargs):
        return redirect("blog:detail", slug=self.get_object())

class BlogCreateView(CreateView):
    form_class = BlogForm
    model = Blog
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context

class BlogUpdateView(UpdateView):
    form_class = BlogForm
    model = Blog
    success_url = '/blog/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blog'


class BlogSearchView(View):

        def get(self, request, *args, **kwargs):
            blogs = Blog.objects.all()
            blog_category_menu = Category.objects.all()
            query = None

            if 'q' in request.GET:
                query= request.GET['q']
                if not query:
                    messages.error(request, "You didn't enter any search criteria!")
                    return redirect(reverse('blog:list'))
                search = Q(title__icontains=query) | Q(content__icontains=query)
                blogs = blogs.filter(search)
    
            context = {
                'search_term': query,
                'blogs': blogs,
                'blog_category_menu': blog_category_menu,
            }
            return render(request, 'blog/blog_search.html', context)