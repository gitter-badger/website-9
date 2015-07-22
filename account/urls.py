from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
   	url(r'^signup$', views.signup, name='signup'),
   	url(r'^login', views.login_view, name='login'),
   	url(r'^logout$', views.logout_view, name='logout'),
   	url(r'^user', views.user_detail, name='user_detail'),
]
