from django.urls import path
from . import views

app_name = 'newsletters'

urlpatterns = [
    path('marketingsubs/', views.marketing_sub, name='marketingsubs'),
]