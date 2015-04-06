from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from registration.backends.simple.views import RegistrationView


class MyRegView(RegistrationView):
    def get_success_url(self, request, user):
        return '/forum/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_forum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('forum.urls')),  # No namespace here.
    url(r'^forum/', include('forum.urls', namespace='forum')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', MyRegView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
            'serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
