from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('hostapp',
    # Examples:
    url(r'^$', 'views.list_host', name='listHost'),
    url(r'^details/(?P<host>[\w.,/_\-]+)/$', 'views.details_host', name='detailsHost'),
    url(r'^memory/(?P<host>[\w.,/_\-]+)/$', 'views.host_memory', name='detailsMemoryHost'),
    url(r'^swap/(?P<host>[\w.,/_\-]+)/$', 'views.host_swap', name='detailsSwapHost'),
)
