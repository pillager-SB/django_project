import uuid
from datetime import timedelta
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


def get_activation_key_expires():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    city = models.CharField(max_length=64, blank=True)
    activation_key = models.UUIDField(default=uuid.uuid4)
    activation_key_expires = models.DateTimeField(default=get_activation_key_expires)

    @property
    def is_activation_key_expired(self):
        return now() > self.activation_key_expires

    def activate(self):
        self.is_active = True
        self.activation_key_expires = now()


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NON_BINARY = 'N'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NON_BINARY, 'Non Binary')
    )
    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, verbose_name='пол')

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs): 
        instance.shopuserprofile.save()
