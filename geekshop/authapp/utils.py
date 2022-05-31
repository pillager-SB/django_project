from urllib.parse import urljoin
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse


def send_verification_mail(user):
    verification_link = urljoin(
        settings.DOMAIN_NAME,
        reverse('auth:verify', args=[user.email, user.activation_key])
    )
    send_mail('Verify you account',
              f'Use this link to verify your account: {verification_link}',
              'no-replay@localhost',
              [user.email],
              fail_silently=True
              )
