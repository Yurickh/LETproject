from django.conf.urls import patterns, include, url
from ELO.views import hello

urlpatterns = patterns('',
	url(r'^hello/$', hello),
)
