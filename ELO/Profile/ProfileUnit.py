#coding: utf-8

from abc import*
from django.shortcuts import render
from django import forms


""" Interface for the User Interface layer of the Profile module.
	It is responsible for ...
"""

class IfUiProfile:
	__metaclass__ = ABCMeta

	"""Causes the creation of the layers."""
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
		if isinstance(value, IfBusProfile):
			self.__bus = value
		else:
			raise TypeError("Expected IfBusProfile instance at UiProfile.__bus. Received " + str(type(value)) + " instead.")

	@bus.deleter
	def bus(self):
		del self.__bus

	"""The main method of any UI class, this method allows the Factory to give this module the control of the program.
	"""
	@abstractmethod
	def run(self, request): pass


""" Interface for the Business layer of the Profile module.
	It is responsible for...
"""
class IfBusProfile:
	__metaclass__ = ABCMeta

	""" Enforces the existance of the underlaying layer """
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
		if isinstance(value, IfPersProfile):
			self.__pers = value
		else:
			raise TypeError("Expected IfPersProfile instance at BusProfile.__pers. Received " + str(type(value)) + "instead.")

	@pers.deleter
	def pers(self):
		del self.__pers


class IfPersProfile: pass

class UiProfile(IfUiProfile): 

	def run(self, request):
		return render(request, "Profile/home.html")


class BusProfile(IfBusProfile): pass

class PersProfile(IfPersProfile): pass
