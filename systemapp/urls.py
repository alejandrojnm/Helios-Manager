from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('systemapp',
    # Examples:
    url(r'^dashboard/$', 'views.dashboard', name='dashboard'),
)
