from django.contrib.auth.decorators import user_passes_test

check_is_superuser = user_passes_test(lambda u: u.is_superuser)
