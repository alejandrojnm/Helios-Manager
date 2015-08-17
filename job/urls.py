from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('job',
    # Examples:
    #url(r'^show/(?P<id>[\w.,/:\,/_\-]+)/$', 'views.showJob', name='showJob'),
    url(r'^show/$', 'views.showJob', name='showJob'),
    url(r'^details/(?P<host>[\w.,/_\-]+)/$', 'views.detailsJob', name='detailsJob'),
    url(r'^deploy/$', 'views.deployJob', name='deployJob'),

    # JSON
    url(r'^show/all/$', 'views.showAllJob', name='showAllJob'),
)
