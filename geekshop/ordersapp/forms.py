from django import forms
from .models import Order, OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ('order',)

    product_price = forms.DecimalField(required=False, disabled=True)
    summary = forms.DecimalField(required=False, disabled=True)


OrderItemFormset = forms.inlineformset_factory(Order, OrderItem, OrderItemForm, extra=1)
