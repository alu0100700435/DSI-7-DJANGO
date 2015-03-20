from django.conf.urls import patterns, include, url

urlpatterns = patterns('staticpages.views',
	url(r'^$', 'index'),
	url(r'^home/$', 'home'),
	url(r'^help/$', 'help'),
	url(r'^about/$', 'about'),
)
