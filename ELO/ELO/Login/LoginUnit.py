from abc import *

class IfUiLogin:

	__metaclass__ = ABCMeta

	@abstractmethod
	def run(self): pass

class IfBusLogin:

	__metaclass__ = ABCMeta

	@abstractmethod
	def validate(username, password): pass

class UiLogin(IfUiLogin):
	
	busLogin = None
	
	def run(self): return {}

	def setBus(self, busClass):
		self.busLogin = busClass

class StubLogin(IfBusLogin):
	def validate(username, password): pass