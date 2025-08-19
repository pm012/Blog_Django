from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login



def register(request):
    """Register a new user"""
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
