from django.db import models

class BlogPost(models.Model):  
    title = models.CharField(max_length=200)
    text = models.TextField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Assuming 'auth.User' is the user model used in your project
    # If you have a custom user model, replace 'auth.User' with your model's name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
