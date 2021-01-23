from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('shipping_info/', views.shipping_info, name='shipping_info'),
    path(
        'order_history/<order_number>',
        views.order_history, name='order_history'
        ),
]
