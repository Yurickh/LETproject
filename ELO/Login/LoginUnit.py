#coding utf-8

from abc import *

class IfUiLogin:
	__metaclass__ = ABCMeta

	@abstractmethod
	def run(self, request): pass

class IfBusLogin: pass
	__metaclas__ = ABCMeta

	@abstractmethod
	def PodeFaze(self): pass

class IfPersLogin: 
	__metaclass__ = ABCMeta
	
class UiLogin(IfUiLogin):

	def run(self, request):
		
		return render()

class BusLogin(IfBusLogin):


class PersLogin(): pass
