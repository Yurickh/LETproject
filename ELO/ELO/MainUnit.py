from abc import *
from Login.LoginUnit import *

from django.core.exceptions import PermissionDenied

#TEMPORARY
from django.shortcuts import render

""" The Factory class is responsible for the building and flow control of the whole program.
	Everything is created by It. It sees everything. It sees you. """
class Factory:
	__ui = None
	__bus = None
	__pers = None

	def runLogin(self, request):
		if not self.__ui is IfUiLogin:
			self.__bus = BusLogin()

			self.__ui = UiLogin(self.__bus)

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
