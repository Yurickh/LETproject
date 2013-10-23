from django.conf.urls import patterns, include, url

from EntityUnit import *

urlpatterns = patterns('',
	url(r'^$', Factory().run()),
)
