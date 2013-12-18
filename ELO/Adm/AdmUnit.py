#coding: utf-8

from abc import*

""" This file is responsible for storing all the layers that deal with the Administrative module.
	The methods here are created and called by the Factory (MainUnit.py) when necessary.
	They're responsible for ...
"""

class IfUiAdm:
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
		if isinstance(value, IfBusAdm):
			self.__bus = value
		else:
			raise TypeError("Expected IfBusAdm instance at UiAdm.__bus. Received " + str(type(value)) + " instead.")

	@bus.deleter
	def bus(self):
		del self.__bus

	@abstractmethod
	def run(self, request): pass


class IfBusAdm:
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
		if isinstance(value, IfPersAdm):
			self.__pers = value
		else:
			raise TypeError("Expected IfPersAdm instance at BusAdm.__pers. Received " + str(type(value)) + " instead.")

	@pers.deleter	
	def pers(self):
		del self.__pers


class IfPersAdm:	pass


class UiAdm(IfUiAdm):	pass

class BusAdm(IfBusAdm):	pass

class PersAdm(IfPersAdm):	pass
