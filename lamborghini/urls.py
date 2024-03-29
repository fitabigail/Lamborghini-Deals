"""lamborghini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lamborghini_deals.urls'), name='lamborghini_deals'),
    path('cars_view/', include('cars_view.urls'), name='cars_view'),
    path('user_account/', include('user_account.urls'), name='user_account'),
    path('enquiry_form/', include('enquiry_form.urls'), name='enquiry_form'),
    path('summernote/', include('django_summernote.urls')),
    path('social_accounts/', include('allauth.urls')),
]

