from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm
from django.http import Http404
from django.contrib.auth.decorators import login_required

def check_blog_ownership(request, post):
    """Check if the logged-in user is the owner of the blog post."""
    if post.owner != request.user:
        raise Http404("You do not have permission to edit this post.")

@login_required
def index(request):
    posts = BlogPost.objects.filter(owner=request.user)  # Only show posts for the logged-in user
    return render(request, 'blogs/index.html', {'posts': posts})

def new_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user  # Set the owner to the logged-in user
            post.save()
            #form.save()
            return redirect('blogs:index')
    else:
        form = BlogPostForm()
    return render(request, 'blogs/new_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    check_blog_ownership(request, post)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogs/edit_post.html', {'form': form})