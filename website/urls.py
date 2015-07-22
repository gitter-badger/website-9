from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	# Examples:
	# url(r'^$', 'website.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('frontend.urls', namespace='frontend')),
	url(r'^accounts/', include('account.urls', namespace='accounts')),
	url(r'^webinar/', include('webinar.urls', namespace='webinar')),
	url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^avatar/', include('avatar.urls')),
]
