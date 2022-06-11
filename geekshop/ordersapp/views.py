from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from utils.mixins import SuperUserRequiredMixin, TitleMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.db import transaction
from django.shortcuts import get_object_or_404


class OrderListView(SuperUserRequiredMixin, TitleMixin, ListView):
    template_name = "ordersapp/order_list.html"
    model = Order
    title = "Заказы"

    def get_queryset(self):
        return Order.objects.order_by('created_at')


@login_required
@transaction.atomic()
def create_order(request):
    basket_items = request.user.basket.all()
    if not basket_items:
        return HttpResponseBadRequest()
    order = Order(user=request.user)
    order.save()
    for item in basket_items:
        item = OrderItem(order=order, product=item.product, quantity=item.quantity)
        item.save()

    basket_items.delete()
    return HttpResponseRedirect(reverse('orders:list'))

@login_required
def pay_for_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if not order.can_pay:
        return HttpResponseBadRequest()

    order.status = Order.PAID
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))


    basket_items.delete()
    return HttpResponseRedirect(reverse('orders:list'))

@login_required
@transaction.atomic()
def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if not order.can_cancel:
        return HttpResponseBadRequest()

    order.status = Order.CANCELED
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))
# class OrderUpdateView(SuperUserRequiredMixin, TitleMixin, UpdateView):
#     template_name = 'adminapp/update_user.html'
#     model = Order
#     form_class = UserEditForm
#     success_url = reverse_lazy("admin:users")
#     title = "Редактирование пользователя"
