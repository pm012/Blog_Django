from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    """Form for creating and updating blog posts."""
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }
        labels = {
            'title': 'Blog Post Title',
            'text': 'Content',
        }