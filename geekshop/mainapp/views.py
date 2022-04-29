from django.shortcuts import render
from .models import Product, Category

MENU_LINKS = {
    'index': 'Главная',
    'products': 'Товары',
    'contact': 'Контакты',
}


def index(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Магазин: Главная',
        'url_name': 'index',
        'menu': MENU_LINKS,
    })


def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'mainapp/products.html', context={
        'title': 'Магазин: Товары',
        'menu': MENU_LINKS,
        'products': products,
        'categories': categories,
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Магазин: Контакты',
        'menu': MENU_LINKS,
    })
