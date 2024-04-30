from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    context = {
        'title': 'home',
        'content': 'content',
        'list': ['first', 'second'],
        'dist': {'first': 1, 'second': 'second'},
        'bool': True
    }
    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    return HttpResponse('О Нас')
