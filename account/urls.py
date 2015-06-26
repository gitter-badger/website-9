from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
   	url(r'^signup$', views.signup, name='signup'),
   	url(r'^login$', views.login, name='login'),
]
