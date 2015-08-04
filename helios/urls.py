from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'loginapp.views.login_helios', name='login'),
    url(r'^login/', 'loginapp.views.loginauth', name='loginauth'),
    url(r'^logout/', 'loginapp.views.logoutauth', name='logoutauth'),
    url(r'^system/', include('systemapp.urls')),
    url(r'^job/', include('jobapp.urls')),
    url(r'^host/', include('hostapp.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
