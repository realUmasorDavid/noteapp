from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='note_image', blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True,  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class meta:
        ordering = ['-created_at']