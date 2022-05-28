from authapp.models import ShopUser
from mainapp.models import Category, Product
from adminapp.forms import (
    RegisterForm,
    UserEditForm,
    CategoryEditForm,
    ProductEditForm
)
from adminapp.utils import check_is_superuser
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class SuperUserRequiredMixin:
    @method_decorator(check_is_superuser)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserListView(SuperUserRequiredMixin, TitleMixin, ListView):
    template_name = "adminapp/users.html"
    model = ShopUser
    title = "Пользователи"
    paginate_by = 2
    p = 1
    page_kwarg = 'my_page'

    def get_queryset(selfs):
        return ShopUser.objects.order_by('date_joined')


class UserCreateView(SuperUserRequiredMixin, TitleMixin, CreateView):
    template_name = "adminapp/create_user.html"
    model = ShopUser
    form_class = RegisterForm
    success_url = reverse_lazy("admin:users")
    title = "Создание пользователя"


class UserUpdateView(SuperUserRequiredMixin, TitleMixin, UpdateView):
    template_name = 'adminapp/update_user.html'
    model = ShopUser
    form_class = UserEditForm
    success_url = reverse_lazy("admin:users")
    title = "Редактирование пользователя"


@check_is_superuser
def delete_user(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin:users'))


class CategoryListView(SuperUserRequiredMixin, TitleMixin, ListView):
    template_name = "adminapp/categories.html"
    model = Category
    title = "Категории"

class CategoryCreateView(SuperUserRequiredMixin, TitleMixin, CreateView):
    template_name = "adminapp/create_category.html"
    model = Category
    form_class = CategoryEditForm
    success_url = reverse_lazy("admin:categories")
    title = "Создание категории"


class CategoryUpdateView(SuperUserRequiredMixin, TitleMixin, UpdateView):
    template_name = "adminapp/update_category.html"
    model = Category
    form_class = CategoryEditForm
    success_url = reverse_lazy("admin:categories")
    title = "Редактирование категории"


@check_is_superuser
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.is_active = False
    category.save()
    return HttpResponseRedirect(reverse('admin:categories'))


@check_is_superuser
def products(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    return render(request, "adminapp/products.html", context={
        "title": f"Категория: {category.name}",
        "products": Product.objects.filter(category=category),
        "category": category,
    })


@check_is_superuser
def create_product(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    form = ProductEditForm(initial={"category": category})
    if request.method == "POST":
        form = ProductEditForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('admin:products', args=[category_pk])
            )

    return render(
        request, 'adminapp/create_product.html',
        context={
            "title": "Создание продукта",
            "category": category,
            "form": form,
        },
    )


@check_is_superuser
def update_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    form = ProductEditForm(instance=product)
    if request.method == "POST":
        form = ProductEditForm(instance=product, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))

    return render(
        request, 'adminapp/update_product.html',
        context={
            "title": "Редактирование продукта",
            "product": product,
            "form": form,
        },
    )


@check_is_superuser
def delete_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    product.is_active = False
    product.save()
    return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))
