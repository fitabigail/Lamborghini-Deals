from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login, name='login'),
    path('singup', views.singup, name='singup'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
