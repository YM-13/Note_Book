from datetime import datetime
from django.db import models


# Create your models here.
class Note(models.Model): 
    id = models.BigAutoField(primary_key=True)
    description = models.TextField() # (text field) 
    title = models.CharField("ОГЛАВЛЕНИЕ", max_length=256) # Engl translate
    created_at = models.DateTimeField(auto_now=True) #(datetime, значение должно запис. автома. при создании объекта)
    updated_at = models.DateTimeField(auto_now_add=True) #(datetime, также записывается автоматически, но при каждом обновлении данных)

Note.objects.all().order_by('title') # добавить сортировку по-умолчанию по полю title
    # добавить кастомное отображение в строке: "<Note(id={id объекта}, title={title модели}>"