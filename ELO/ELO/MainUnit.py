from abc import *
from Login.LoginUnit import IfUiLogin, IfBusLogin, UiLogin, BusLogin

from django.shortcuts import render

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

	def runLogout(self, request):
		del request.session['USER']
		return self.runLogin(request)

	def runProfile(self, request):
		return render(request, "profile.html", {'user': request.session['USER']})

class IfPers:
	__metaclass__ = ABCMeta

class Pers: pass
