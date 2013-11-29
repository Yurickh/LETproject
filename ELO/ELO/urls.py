#encode: utf-8
""" This file is responsible for reading the URL of the requests and redirecting the program to the factory that will create an object for the page creation """

from django.conf.urls import patterns, url
from ELO.MainUnit import Factory

factory = Factory()

urlpatterns = patterns('', 
	url(r'^$', factory.runLogin),
	url(r'^profile$', factory.runProfile),
	url(r'^logout$', factory.runLogout),
)
