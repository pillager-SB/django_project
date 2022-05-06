from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product
from django.urls import reverse


def basket(request):
    return render(request, 'basketapp/basket.html', context={
        'basket': Basket.objects.filter(user=request.user)
    })


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product)
    if basket:
        basket_item = basket[0]
        basket_item.quantity += 1
        basket_item.save()
    else:
        basket_item = Basket(user=request.user, product=product)
        basket_item.quantity += 1
        basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('index')))


def basket_remove(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.quantity -= 1
    if not basket.quantity:
        basket.delete()
    else:
        basket.save()
    return HttpResponseRedirect(reverse('basket:view'))

