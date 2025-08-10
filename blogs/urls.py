from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_post, name='new_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
]