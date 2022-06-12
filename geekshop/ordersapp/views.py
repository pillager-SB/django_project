from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory

from ordersapp.forms import OrderItemForm
from ordersapp.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from utils.mixins import LoginRequiredMixin, TitleMixin
from django.views.generic import ListView, UpdateView
from django.db import transaction


class OrderListView(LoginRequiredMixin, TitleMixin, ListView):
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


class OrderUpdateView(LoginRequiredMixin, TitleMixin, UpdateView):
    template_name = 'ordersapp/order_update.html'
    model = Order
    success_url = reverse_lazy("orders:list")
    title = "Редактирование заказа"
    fields = ()

    def get_context_data(self, **kwargs):
        OrderItemFormset = inlineformset_factory(Order, OrderItem, OrderItemForm, extra=2)
        formset = OrderItemFormset(instance=self.object)
        context = super().get_context_data(**kwargs)
        context['orderitems'] = formset
        return context

    @transaction.atomic
    def form_valid(self, form):
        OrderItemFormset = inlineformset_factory(Order, OrderItem, OrderItemForm, extra=2)
        formset = OrderItemFormset(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.save()
        return super().form_valid(form)
