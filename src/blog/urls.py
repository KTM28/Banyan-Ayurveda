from django.urls import path
from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    CategoryView,
)

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/',  BlogCreateView.as_view(), name='create'),
    path('<slug>/', BlogDetailView.as_view(), name='detail'),
    path('<slug>/update/', BlogUpdateView.as_view(), name='update'),
    path('<slug>/delete/',  BlogDeleteView.as_view(), name='delete'),
    path('category/<str:category>/', CategoryView, name='category'),
]
