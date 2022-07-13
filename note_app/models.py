from datetime import datetime
from django.db import models


# Create your models here.
class Note(models.Model): 
    description = models.TextField()
    title = models.CharField("title", max_length=256)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['title']


    def __str__(self):
        return f"<Note(id={self.id}, title={self.title})>"
        