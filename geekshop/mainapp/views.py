from django.shortcuts import render
from django.urls import reverse

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
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Магазин: Контакты',
        'menu': MENU_LINKS,
    })
