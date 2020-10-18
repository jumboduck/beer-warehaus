from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_producer/', views.add_producer, name='add_producer'),
    path('producers/', views.producers, name='producers'),
    path('add_product/', views.add_product, name='add_product'),
]
