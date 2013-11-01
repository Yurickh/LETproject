from django.conf.urls import patterns, url
from MainUnit import Factory

urlpatterns = patterns('',
	url(r'^$', Factory().runLogin),
)