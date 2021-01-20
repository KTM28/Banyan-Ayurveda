from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from profiles.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog, BlogView, Like, Comment, Category
from .forms import BlogForm, CommentForm

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
        """ Add Comment to the Post """
        form = CommentForm(self.request.POST)
        if form.is_valid():
            blog = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.blog = blog
            comment.save()
            return redirect("blog:detail", slug=blog.slug)
        return redirect("blog:detail", slug=self.get_object().slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        })
        return context

    def get_object(self, **kwargs):
        """Counts the number of authenticated users views of the blog."""
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            BlogView.objects.get_or_create(user=self.request.user, blog=object)
        return object


class BlogCreateView(LoginRequiredMixin, CreateView):
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

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    form_class = BlogForm
    model = Blog
    success_url = '/blog/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = '/blog'


class BlogSearchView(View):
        template_name = 'blog/blog_search.html'

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

class BlogAuthorProfileView(LoginRequiredMixin, View):
    model = UserProfile
    template_name = 'blog/blog_author.html'
    context_object_name = 'user'

    def get(self, request, *args, **kwargs):
        page_user = get_object_or_404(User, id=self.kwargs['pk'])
        user_blog = Blog.objects.filter(
            author=page_user.id).order_by('-publish_date')
        context = {
            'page_user': page_user,
            'user_blog': user_blog,
        }
        return render(request, 'blog/blog_author.html', context)

@ login_required()
def LikeBlog(request, slug):

    blog = get_object_or_404(Blog, slug=slug)
    like_queryset = Like.objects.filter(user=request.user, blog=blog)

    if like_queryset.exists():
        # If there is like in post then take away the like
        like_queryset[0].delete()
        return redirect('blog:detail', slug=slug)

    Like.objects.create(user=request.user, blog=blog)
    return redirect('blog:detail', slug=slug)