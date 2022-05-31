from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('edit/', authapp.edit, name='edit'),
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path("verify/<str:email>/<str:key>", authapp.verify, name="verify")
]
