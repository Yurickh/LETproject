from abc import *
from Login.LoginUnit import IfUiLogin, IfBusLogin, UiLogin, BusLogin

from django.shortcuts import render
from django.http import Http404

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
		if 'USER' in request.session.keys():
			del request.session['USER']
		return self.runLogin(request)

	def runProfile(self, request):
		if 'USER' in request.session.keys():
			return render(request, "profile.html", {'user': request.session['USER']})
		else:
			raise Http404("You cant access this page")

class IfPers:
	__metaclass__ = ABCMeta

class Pers: pass
