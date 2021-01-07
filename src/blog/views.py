from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog, BlogView, Like, Comment, Category


class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog

class BlogUpdateView(UpdateView):
    model = Blog

class BlogDeleteView(DeleteView):
    model = Blog
    
