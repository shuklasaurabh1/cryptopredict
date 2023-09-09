# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crypto/', views.cryptocurrency_list, name='cryptocurrency_list'),
]
