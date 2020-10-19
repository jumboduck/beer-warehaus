from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_producer/', views.add_producer, name='add_producer'),
    path('', views.producers, name='producers'),
]
