from authapp.forms import UserEditForm, LoginForm, RegisterForm, UserProfileEditForm
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from .models import ShopUser
from .utils import send_verification_mail
from django.db import transaction


def login(request):
    title = 'Вход в систему'
    login_form = LoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user=user)
            redirect_url = request.GET.get('next', reverse('index'))
            return HttpResponseRedirect(redirect_url)

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def register(request):
    title = 'Регистрация'
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            send_verification_mail(user)
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = RegisterForm()
    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)


@transaction.atomic
@login_required
def edit(request):
    title = 'Редактирование'
    user_form = UserEditForm(instance=request.user)
    profile_form = UserProfileEditForm(instance=request.user.profile)
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        profile_form = UserProfileEditForm(instance=request.user.profile, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse("index"))

    return render(request,
                  'authapp/edit.html',
                  context={
                      'title': title,
                      'user_form': user_form,
                      'profile_form': profile_form
                  },
                  )


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def verify(request, email, key):
    try:
        user = ShopUser.objects.get(email=email, activation_key=key)
        if user.is_activation_key_expired:
            return render(request, "authapp/verification.html", context={'message': 'Key is expired'})
        user.activate()
        user.save()
        return render(request, "authapp/verification.html", context={'message': 'Success'})
    except ShopUser.DoesNotExist:
        return render(request, "authapp/verification.html", context={'message': 'Verification failed'})
