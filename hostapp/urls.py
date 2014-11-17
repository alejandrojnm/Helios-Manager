from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('hostapp',
    # Examples:
    url(r'^list/$', 'views.list_host', name='listHost'),
)
