from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('staticpages.views',
	url(r'^$', 'index'),
	url(r'^home/$', 'home'),
	url(r'^help/$', 'help'),
	url(r'^about/$', 'about'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
