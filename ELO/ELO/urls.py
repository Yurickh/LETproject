#encode: utf-8
""" This file is responsible for reading the URL of the requests and redirecting the program to the factory that will create an object for the page creation """

from django.conf.urls import patterns, url

urlpatterns = patterns('ELO.MainUnit', url(r'^$', Factory().runLogin()))
)
