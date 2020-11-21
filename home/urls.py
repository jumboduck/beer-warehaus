from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('manage_slides/', views.manage_slides, name='manage_slides'),
    path('manage_slides/add/', views.add_slide, name='add_slide'),
    path('manage_slides/edit/<int:slide_id>/', views.edit_slide, name='edit_slide'),
    path('manage_slides/delete/<int:slide_id>/', views.delete_slide, name='delete_slide'),
]
