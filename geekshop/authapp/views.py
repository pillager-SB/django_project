from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from authapp.forms import EditForm, LoginForm, RegisterForm


def login(request):
    title = 'Вход в систему'
    login_form = LoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def register(request):
    title = 'Регистрация'
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = RegisterForm()
    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)


def edit(request):
    title = 'Редактирование'
    if request.method == 'POST':
        edit_form = EditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = EditForm(instance=request.user)
    content = {'title': title, 'edit_form': edit_form}
    return render(request, 'authapp/edit.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
