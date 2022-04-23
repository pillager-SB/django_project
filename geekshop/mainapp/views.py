from django.shortcuts import render
from django.urls import reverse
import json

MENU_LINKS = {
    'index': 'Главная',
    'products': 'Товары',
    'contact': 'Контакты',
}


def index(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Магазин: Главная',
        'menu': MENU_LINKS,
    })


def products(request):
    return render(request, 'mainapp/products.html', context={
        'title': 'Магазин: Товары',
        'menu': MENU_LINKS,
        'products': [
            {
                "name": "Стул 1",
                "description": "отличный стул!",
                "image": "/img/product-11.jpg"
            },
            {
                "name": "Стул 2",
                "description": "сесть - не встать!",
                "image": "/img/product-21.jpg"
            },
            {
                "name": "Стул 3",
                "description": "для себя - любимого!",
                "image": "/img/product-31.jpg"
            }
        ],
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Магазин: Контакты',
        'menu': MENU_LINKS,
    })
