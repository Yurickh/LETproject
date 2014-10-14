#coding: utf-8

from abc import*

import ELO.locale.index as lang

from django.shortcuts import render
from django.core.exceptions import PermissionDenied

class IfUiCourse:
	__metaclass__ = ABCMeta

	def __init__(self, bus):
		try:
			self.bus = bus
		except TypeError as exc:
			del self
			raise exc

	@property
	def bus(self):
		return self.__bus

	@bus.setter
	def bus(self, value):
		if isinstance(value, IfBusCourse):
			self.__bus = value
		else:
			raise TypeError("Expected IfBusCourse instance at UiCourse.__bus. Received " + str(type(value)) + " instead.")

	@bus.deleter
	def bus(self):
		del self.__bus

	@abstractmethod
	def run(self, request, courseid): pass


class IfBusCourse:
	__metaclass__ = ABCMeta

	def __init_(self, pers):
		try:
			self.pers = pers
		except TypeError as exc:
			del self
			raise exc

	@property
	def pers(self):
		return self.__pers
	
	@pers.setter
	def pers(self, value):
		if isinstance(value, IfPersCourse):
			self.__pers = value
		else:
			raise TypeError("Expected IfPersCourse instance at BusCourse.__pers. Received " + str(type(value)) + "instead.")

	@pers.deleter
	def pers(self):
		del self.__pers

class IfPersCourse: pass


class UiCourse(IfUiCourse):

	def run(self, request, courseid):
		
		user = request.session['user']

		if courseid in user['course']:
			print 'yey'
			return HttpResponseRedirect('/') ## TODO: everything
		else:
			raise PermissionDenied(lang.DICT["EXCEPTION_403_STD"])
		

class BusCourse(IfBusCourse):	pass

class PersCourse(IfPersCourse):	pass
