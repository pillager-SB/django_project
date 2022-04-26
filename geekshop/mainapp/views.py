from django.shortcuts import render
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
    with open('products.JSON', 'r', encoding='utf-8') as f:
        products_lst = json.load(f)
    return render(request, 'mainapp/products.html', context={
        'title': 'Магазин: Товары',
        'menu': MENU_LINKS,
        'products': products_lst,
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Магазин: Контакты',
        'menu': MENU_LINKS,
    })
