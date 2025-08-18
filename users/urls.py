from django.urls import path, include
from django.contrib.auth import views as auth_views
from .froms import CustomAuthenticationForm
from . import views

app_name = 'users'

urlpatterns = [
    #Add URL auth (authentication)
    path('login/', auth_views.LoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]