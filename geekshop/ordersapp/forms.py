from django import forms
from .models import Order, OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ('order',)
    product_price = forms.DecimalField(disabled=True)
    summary = forms.DecimalField(disabled=True)

OrderItemFormset = forms.inlineformset_factory(Order, OrderItem, OrderItemForm, extra=2)
