from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', include('staticpages.urls')),
	url(r'^staticpages/', include('staticpages.urls')),
	url(r'^home/$', 'staticpages.views.home'),
	url(r'^help/$', 'staticpages.views.help'),
	url(r'^about/$', 'staticpages.views.about'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
