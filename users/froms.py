from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'maxlength': 30, 'class': 'form-control', 'style': 'max-width: 300px;'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'maxlength': 30, 'class': 'form-control', 'style': 'max-width: 300px;'})
    )