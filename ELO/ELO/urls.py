from django.conf.urls import patterns, include, url

from kernel.MainUnit import Factory

urlpatterns = patterns('',
	url(r'^$', Factory().run()),
)