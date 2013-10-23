from django.conf.urls import patterns, include, url
from ELO.views import index

urlpatterns = patterns('',
	url(r'^$', index),

