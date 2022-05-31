from django.urls import path
import adminapp.views as adminapp

app_name = 'admin'


urlpatterns = [
    path("users/", adminapp.UserListView.as_view(), name="users"),
    path("users/<int:my_page>", adminapp.UserListView.as_view(), name="users"),
    path("users/create/", adminapp.UserCreateView.as_view(), name="create_user"),
    path("users/update/<int:pk>/", adminapp.UserUpdateView.as_view(), name="update_user"),
    path("users/delete/<int:pk>/", adminapp.delete_user, name="delete_user"),

    path("categories/", adminapp.CategoryListView.as_view(), name="categories"),
    path("categories/create/", adminapp.CategoryCreateView.as_view(), name="create_category"),
    path("categories/update/<int:pk>/", adminapp.CategoryUpdateView.as_view(), name="update_category"),
    path("categories/delete/<int:pk>/", adminapp.delete_category, name="delete_category"),

    path("products/<int:category_pk>/", adminapp.products, name="products"),
    path("products/<int:category_pk>/create/", adminapp.create_product, name="create_product"),
    path("products/update/<int:product_pk>/", adminapp.update_product, name="update_product"),
    path("products/delete<product_pk>/", adminapp.delete_product, name="delete_product"),
]