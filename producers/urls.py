from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.producers, name='producers'),
    path('<int:producer_id>/', views.producer_detail, name='producer_detail'),
    path('add/', views.add_producer, name='add_producer'),
    path('manage/', views.manage_producers, name='manage_producers'),
    path('edit/<int:producer_id>/', views.edit_producer, name='edit_producer'),
    path('delete/<int:producer_id>/', views.delete_producer, name='delete_producer'),
]
