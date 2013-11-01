#encode: utf-8

from Login.LoginUnit import UiLogin, BusLogin, PersLogin
from Login.forms import LoginForm

class Factory(object):

	__ui = None
	__bus = None
	__pers = None

	def runLogin(self, request):
		if not self.__ui is UiLogin:
			self.__ui = UiLogin()
			self.__bus = BusLogin()
			self.__pers = PersLogin()

			self.__ui.setBus(self.__bus)
			self.__bus.setPers(self.__pers)

		return self.__ui.run(request)