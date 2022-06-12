from django.urls import path
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path("", ordersapp.OrderListView.as_view(), name="list"),
    path("create", ordersapp.create_order, name="create"),
    path("<int:pk>", ordersapp.OrderUpdateView.as_view(), name="update"),
    path("<int:pk>/pay", ordersapp.pay_for_order, name="pay"),
    path("<int:pk>/cancel", ordersapp.cancel_order, name="cancel"),
]
