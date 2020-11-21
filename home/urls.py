from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('manage_slides/', views.manage_slides, name='manage_slides'),
]
