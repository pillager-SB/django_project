from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ShopUser

# Register your models here.

@admin.register(ShopUser)
class ShopUserAdmin(UserAdmin):

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return [
            *super().get_fieldsets(request, obj),
            ('Custom fields', {'fields': ('city',)})
        ]