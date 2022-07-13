# Здесь связь с файлом note_app/urls.py
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

def note_app_home(request):
    return render(request, 'note_app/home_page.html', {'title': 'HOME PAGE'})
