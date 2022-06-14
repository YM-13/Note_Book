from django.db import models

# Create your models here.
class Note(models.Model):
    pass
    id = models.BigAutoField(primary_key=True) # (integer значение)
    description = models. # (text field) 
    title = models.CharField(_("ОГЛАВЛЕНИЕ"), max_length=256)
    created_at (datetime, значение должно запис. автома. при создании объекта) = models.
    updated_at (datetime, также записывается автоматически, но в при каждом обновлении данных) = models.
    updated_at (datetime, также записывается автоматически, но в при каждом обновлении данных) = models.
    # добавить сортировку по-умолчанию по полю title
    # добавить кастомное отображение в строке: "<Note(id={id объекта}, title={title модели}>"