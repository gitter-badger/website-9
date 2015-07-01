from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	# Examples:
	   url(r'^course$', views.course_view, name='course_view'),
]
