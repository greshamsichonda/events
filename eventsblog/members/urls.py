
from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='log-out'),
    path('register_user/', views.register_user, name='register-user'),
]