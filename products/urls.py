from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_producer/', views.add_producer, name='add_producer'),
    path('find_untappd_producer/', views.find_untappd_producer, name='find_untappd_producer'),
    path('add_untappd_producer/', views.add_untappd_producer, name='add_untappd_producer'),
    path('producers/', views.producers, name='producers'),
    path('add_product/', views.add_product, name='add_product'),
    path('find_untappd_product/', views.find_untappd_product, name='find_untappd_product'),
    # path('add_untappd_product/', views.add_untappd_product, name='add_untappd_product'),
]
