from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_details, name='product_details'),
    path('services/', views.all_services, name='services'),
    path('services/<int:treatment_id>', views.service_details, name='service_details'),
]
