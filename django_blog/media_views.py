# django_blog/media_views.py
from django.views.static import serve
from django.conf import settings
from django.http import Http404

def serve_media(request, path):
    if not settings.DEBUG:
        # Security check - ensure the path is within media directory
        if not path.startswith('profile_images/') and not path.startswith('avatars/'):
            raise Http404("Media not found")
        
        # Serve the file using Django's serve view
        return serve(request, path, document_root=settings.MEDIA_ROOT)
    else:
        # In development, let Django handle it normally
        from django.views.static import serve as dev_serve
        return dev_serve(request, path, document_root=settings.MEDIA_ROOT)