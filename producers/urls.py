from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.producers, name='producers'),
    path('add_producer/', views.add_producer, name='add_producer'),
    path('edit/<int:producer_id>/', views.edit_producer, name='edit_producer'),
]
