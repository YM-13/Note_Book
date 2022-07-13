"""Проверь как у Портиллы. Сначала здесь было пусто. Я смотрел русского https://www.youtube.com/watch?v=o6ac2T8fhhM&list=PLDyJYA6aTY1nZ9fSGcsK4wqeu-xaJksQQ&index=17
на 3:38"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_app_home, name='note_app_home'),
]
