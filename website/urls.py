from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

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
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))