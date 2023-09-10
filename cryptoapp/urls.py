# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crypto/', views.cryptocurrency_list, name='cryptocurrency_list'),
    path('crypto/<str:cryptocurrency_id>/', views.cryptocurrency_detail, name='crypto_detail'),
    path('crypto/history/chart/<str:crypto_id>/', views.crypto_history_chart, name='crypto_history_chart'),


]
