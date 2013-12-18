#coding: utf-8

""" This file is responsible for reading the URL of the requests and redirecting the program to the factory that will create an object for the page creation """

from django.conf.urls import patterns, url
from ELO.MainUnit import Factory

factory = Factory()

urlpatterns = patterns('', 
	url(r'^$', factory.runLogin, {'entity': 'Student'}),
	url(r'^proflogin$', factory.runLogin, {'entity': 'Professor'}),
	url(r'^364fd8cdc3a35a89b7be75bc9d10ebea$', factory.runLogin, {'entity': 'Adm'}),
	url(r'^profile$', factory.runProfile),
	url(r'^logout$', factory.runLogout),
	url(r'^course', factory.runCourse),
	url(r'^administracao', factory.runAdm),
)
