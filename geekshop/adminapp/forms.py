from authapp.models import ShopUser
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username',)

class UserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'avatar', 'email', 'city')
