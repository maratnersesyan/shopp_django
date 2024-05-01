from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',

    }
    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context = {
        'title': 'Home - О Нас',
        'content': 'Наши контакты',
        'text_on_page': 'Текст о том, почему магазин такой классный'
    }
    return render(request, 'main/about.html', context)

def delivery(request) -> HttpResponse:
    context = {
        'title': 'Способы доставки',
        'content': 'Интернет-магазин выполняет доставку любого товара своей собственной Службой доставки.',
    }
    return render(request, 'main/delivery.html', context)

def contact(request) -> HttpResponse:
    context = {
        'title': 'Контакты',
        'tel': '8 (800) 234-50-60',
        'time': 'Время работы Call-центра:',
        'times': 'ежедневно с 10:00 до 20:00',
        'content': 'В нашем магазине всегда только самые лучшие товары по низким ценам. Каталог продаваемых товаров постоянно пополняется и обновляется.',
    }
    return render(request, 'main/contact.html', context)


