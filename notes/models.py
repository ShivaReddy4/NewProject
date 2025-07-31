# notes/models.py

from django.db import models
from django.utils import timezone  # ✅ this is the key missing line

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    created_at = models.DateTimeField(default=timezone.now)

    
# using timezone.now he

    

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100, default='0000000000000')
    publication_year = models.IntegerField(default=2023)
    isbn = models.CharField(max_length=13, default='0000000000000')

    class Meta:
        ordering = ['-created_at']  

    def __str__(self):
        return self.title