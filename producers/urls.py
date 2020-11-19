from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.producers, name='producers'),
    path('<int:producer_id>/', views.producer_detail, name='producer_detail'),
    path('add_producer/', views.add_producer, name='add_producer'),
    path('manage_producers/', views.manage_producers, name='manage_producers'),
    path('edit/<int:producer_id>/', views.edit_producer, name='edit_producer'),
]
