from django.urls import path, include

app_name = 'users'

urlpatterns = [
    #Add URL auth (authentication)
    path('', include('django.contrib.auth.urls')),
]