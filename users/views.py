from .forms import CustomUserCreationForm, ProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Profile



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

# @login_required
# def profile(request):
#     """Display user profile"""
#     return render(request, 'users/profile.html')

@login_required
def profile(request):
    """Display and update user profile"""
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=profile)

    context = {'profile_form': form, 'profile': profile}
    return render(request, 'users/profile.html', context)