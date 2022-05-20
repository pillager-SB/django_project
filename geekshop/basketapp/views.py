from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from basketapp.models import Basket
from mainapp.models import Product
from django.urls import reverse


@login_required
def basket(request):
    return render(
        request,
        'basketapp/basket.html',
        context={
            'title': "Корзина"}
    )

@login_required
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
    if 'next' in request.META.get("HTTP_REFERER"):
        redirect_url = reverse("index")
    else:
        redirect_url = request.META.get("HTTP_REFERER", reverse("index"))
    return HttpResponseRedirect(redirect_url)

@login_required
def basket_remove(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.quantity -= 1
    if not basket.quantity:
        basket.delete()
    else:
        basket.save()
    return HttpResponseRedirect(reverse('basket:view'))

