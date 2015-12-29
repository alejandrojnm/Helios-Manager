from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'login.views.login_helios', name='login'),
                       url(r'^login/', 'login.views.loginauth', name='loginauth'),
                       url(r'^logout/', 'login.views.logoutauth', name='logoutauth'),
                       url(r'^system/', include('system.urls')),
                       url(r'^job/', include('job.urls')),
                       url(r'^host/', include('host.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )
