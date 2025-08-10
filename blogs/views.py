from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blogs/index.html', {'posts': posts})

def new_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogPostForm()
    return render(request, 'blogs/new_post.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogs/edit_post.html', {'form': form})