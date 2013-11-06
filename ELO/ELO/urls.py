#encode: utf-8

from django.conf.urls import patterns, url
from ELO import MainUnit

urlpatterns = patterns('MainUnit',
	url(r'^$', Factory().runLogin),
)