from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomAuthenticationForm

app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=CustomAuthenticationForm,
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # Optional extra pages (Terms, Privacy, Help)
    path("terms/", auth_views.TemplateView.as_view(template_name="users/terms.html"), name="terms"),
    path("privacy/", auth_views.TemplateView.as_view(template_name="users/privacy.html"), name="privacy"),
    path("help/", auth_views.TemplateView.as_view(template_name="users/help.html"), name="help"),
    path("profile/", views.profile, name="profile"),
]
