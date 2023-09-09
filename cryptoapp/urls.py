# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crypto/', views.cryptocurrency_list, name='cryptocurrency_list'),
    path('crypto/<str:cryptocurrency_id>/', views.cryptocurrency_detail, name='crypto_detail'),

]
