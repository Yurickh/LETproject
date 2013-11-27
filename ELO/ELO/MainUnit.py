from abc import *
from Login.LoginUnit import IfUiLogin, IfBusLogin, UiLogin, BusLogin

class Factory:
	__ui = None
	__bus = None
	__pers = None

	def runLogin(self, request):
		if not self.__ui is IfUiLogin:
			self.__ui = UiLogin()
			self.__bus = BusLogin()
			self.__pers = Pers()

			self.__ui.setBusLogin(self.__bus)
			self.__bus.setPers(self.__pers)

		return self.__ui.run(request)

class IfPers:
	__metaclass__ = ABCMeta

class Pers: pass
