from abc import *
from Login.LoginUnit import *

from django.core.exceptions import PermissionDenied

#TEMPORARY
from django.shortcuts import render

class Factory:
	__ui = None
	__bus = None
	__pers = None

	def runLogin(self, request):
		if not self.__ui is IfUiLogin:
			self.__ui = UiLogin()
			self.__pers = Pers()

			self.__ui = UiLogin(__bus)

		return self.__ui.run(request)

	def runLogout(self, request):
		if 'USER' in request.session.keys():
			del request.session['USER']
		return self.runLogin(request)

	def runProfile(self, request):
		if 'USER' in request.session.keys():
			#TEMPORARY
			return render(request, "profile.html", {'user': request.session['USER']})
		else:
			raise PermissionDenied("You cant access this page")

class IfPers:
	__metaclass__ = ABCMeta

class Pers: pass
