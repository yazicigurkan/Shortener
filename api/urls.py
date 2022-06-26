"""Shortener URL Configuration

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
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Shortener API')

from django.conf.urls import url
from django.urls import path
from .views import CreateShortUrlView ,ListUrlsView, redirect

urlpatterns = [
    path('createurl/',CreateShortUrlView.as_view(),name='Create-Url'),
    path('listurl/',ListUrlsView.as_view(),name="List-Url"),
    path('<str:shortpath>',redirect),
    url('docs/', schema_view, name="docs"),

]