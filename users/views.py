from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Show empty registration form
        form = UserCreationForm()
    else:
        # Handle filled form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Authenticate user and redirect him to main page
            login(request, new_user)
            return redirect('blogs:index')
        # Show empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
