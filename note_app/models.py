from datetime import datetime
from django.db import models


# Create your models here.
class Note(models.Model): 
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()
    title = models.CharField("TITLE", max_length=256)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['title']


    def __str__(self):
        return self.id, self.title