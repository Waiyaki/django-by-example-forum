from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^forum/(?P<pk>\d+)/$', views.forum, name='forum'),
    url(r'^thread/(?P<pk>\d+)/$', views.thread, name='thread'),
)
