from django.urls import path
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path("", ordersapp.OrderListView.as_view(), name="list"),
    path("create", ordersapp.create_order, name="create")
]
