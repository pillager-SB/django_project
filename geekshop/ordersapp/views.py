from .models import Order
from django.views.generic import ListView, CreateView, UpdateView
from utils.mixins import SuperUserRequiredMixin, TitleMixin


class OrderListView(SuperUserRequiredMixin, TitleMixin, ListView):
    template_name = "ordersapp/order_list.html"
    model = Order
    title = "Заказы"

    def get_queryset(self):
        return Order.objects.order_by('created_at')


# class OrderCreateView(SuperUserRequiredMixin, TitleMixin, CreateView):
#     template_name = "adminapp/create_user.html"
#     model = Order
#     form_class = RegisterForm
#     success_url = reverse_lazy("admin:Orders")
#     title = "Создание пользователя"
#
#
# class OrderUpdateView(SuperUserRequiredMixin, TitleMixin, UpdateView):
#     template_name = 'adminapp/update_user.html'
#     model = Order
#     form_class = UserEditForm
#     success_url = reverse_lazy("admin:users")
#     title = "Редактирование пользователя"
