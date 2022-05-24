from django.urls import path
import adminapp.views as adminapp

app_name = 'admin'


urlpatterns = [
    path("users/", adminapp.users, name="users"),
    path("users/create/", adminapp.create_user, name="create_user"),
    path("users/update/<int:pk>/", adminapp.update_user, name="update_user"),
    path("users/delete/<int:pk>/", adminapp.delete_user, name="delete_user"),

    path("categories/", adminapp.categories, name="categories"),
    path("categories/create", adminapp.create_category, name="create_category"),
    path("categories/update/<int:pk>/", adminapp.update_category, name="update_category"),
    path("categories/delete/<int:pk>/", adminapp.delete_category, name="delete_category"),

    path("products/<int:pk>/", adminapp.products, name="products"),
    path("products/<int:pk>/create", adminapp.create_product, name="create_product"),
    path("products/update<int:pk>/", adminapp.update_product, name="update_product"),
    path("products/delete<int:pk>/", adminapp.delete_product, name="delete_product"),
]