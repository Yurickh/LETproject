#coding: utf-8

from abc import*

import ELO.index as lang

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

	def __init__(self, pers):
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

	@abstractmethod
	def getCourse(self, user, courseid): pass

class IfPersCourse:

	@abstractmethod
	def fetch(id, db): pass


class UiCourse(IfUiCourse):

	def run(self, request, courseid):
		
		user = request.session['user']

		if request.method == "GET":
			if courseid in user['courses']:
				course = self.bus.getCourse(user, courseid)
				return render(request, "Course/frame.html", {'course':course})
			else:
				raise PermissionDenied(lang.DICT["EXCEPTION_403_STD"])
		

class BusCourse(IfBusCourse):

	def getCourse(self, user, courseid):
		return True

class PersCourse(IfPersCourse):

	def fetch(id, db):
		return False
