from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('manage_slides/', views.manage_slides, name='manage_slides'),
    path('manage_slides/edit/<int:slide_id>/', views.edit_slide, name='edit_slide'),
]
