from django.contrib.auth import get_user_model
from django.db import models, transaction
from mainapp.models import Product
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Order(models.Model):
    CREATED = "CREATED"
    PAID = "PAID"
    SENT = "SENT"
    DELIVERED = "DELIVERED"
    CANCELED = "CANCELED"

    STATUS_CHOICES = [
        (CREATED, "Создан"),
        (PAID, "Оплачен"),
        (SENT, "Отправлен"),
        (DELIVERED, "Доставлен"),
        (CANCELED, "Отменен")
    ]
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="orders"
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default=CREATED)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def can_pay(self):
        return self.status == Order.CREATED

    @property
    def can_cancel(self):
        return self.status in [Order.CREATED, Order.PAID, Order.SENT]


class OrderItemsManager(models.Manager):
    def quantity(self):
        return sum(item.quantity for item in self.all())

    def sum(self):
        return sum(item.product.price * item.quantity for item in self.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)

    objects = OrderItemsManager()

    @property
    def cost(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'{self.product} - {self.quantity} шт.)'


@receiver(pre_save, sender=OrderItem)
def update_product_quantity(sender, instance, **kwargs):
    old_order_item = OrderItem.objects.filter(pk=instance.pk).first()
    if old_order_item:
        quantity_delta = instance.quantity - old_order_item.quantity
        instance.product.quantity -= quantity_delta
    else:
        instance.product.quantity -= instance.quantity

    instance.product.save()
