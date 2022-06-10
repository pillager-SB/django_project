from django.core.management.base import BaseCommand
from authapp.models import ShopUser, ShopUserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = ShopUser.objects.all()
        for user in users:
            profile = ShopUserProfile.objects.filter(user=user).first()
            if not profile:
                profile = ShopUserProfile(user=user)
                profile.save()
