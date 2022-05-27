from django.urls import path
import adminapp.views as adminapp

app_name = 'admin'


urlpatterns = [
    path("users/", adminapp.UserList.as_view(), name="users"),
    path("users/create/", adminapp.create_user, name="create_user"),
    path("users/update/<int:pk>/", adminapp.update_user, name="update_user"),
    path("users/delete/<int:pk>/", adminapp.delete_user, name="delete_user"),

    path("categories/", adminapp.CategoryList.as_view(), name="categories"),
    path("categories/create/", adminapp.create_category, name="create_category"),
    path("categories/update/<int:pk>/", adminapp.update_category, name="update_category"),
    path("categories/delete/<int:pk>/", adminapp.delete_category, name="delete_category"),

    path("products/<int:category_pk>/", adminapp.products, name="products"),
    path("products/<int:category_pk>/create/", adminapp.create_product, name="create_product"),
    path("products/update/<int:product_pk>/", adminapp.update_product, name="update_product"),
    path("products/delete<product_pk>/", adminapp.delete_product, name="delete_product"),
]