from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Order



class OrderListView(SuperUserRequiredMixin, TitleMixin, ListView):
    template_name = "adminapp/users.html"
    model = ShopUser
    title = "Пользователи"
    paginate_by = 2
    p = 1
    page_kwarg = 'my_page'

    def get_queryset(selfs):
        return ShopUser.objects.order_by('date_joined')


class OrderCreateView(SuperUserRequiredMixin, TitleMixin, CreateView):
    template_name = "adminapp/create_user.html"
    model = ShopUser
    form_class = RegisterForm
    success_url = reverse_lazy("admin:Orders")
    title = "Создание пользователя"


class OrderUpdateView(SuperUserRequiredMixin, TitleMixin, UpdateView):
    template_name = 'adminapp/update_user.html'
    model = ShopUser
    form_class = UserEditForm
    success_url = reverse_lazy("admin:users")
    title = "Редактирование пользователя"
