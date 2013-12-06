#coding: utf-8

from abc import *
from Login.LoginUnit import *

from django.core.exceptions import PermissionDenied

#TEMPORARY
from django.shortcuts import render

def globalContext(request):
	return {
			'user': request.session['user'] if ('user' in request.session.keys()) else False,
		}

""" The Factory class is responsible for the building and flow control of the whole program.
	Everything is created by It. It sees everything. It sees you. """
class Factory:
	__ui = None
	__bus = None
	__pers = None

	def runLogin(self, request):
		if not self.__ui is IfUiLogin:
			self.__pers = PersLogin()
			self.__bus = BusLogin(self.__pers)

			self.__ui = UiLogin(self.__bus)

		return self.__ui.run(request)

	def runLogout(self, request):
		if 'user' in request.session.keys():
			del request.session['user']
		return self.runLogin(request)

	def runProfile(self, request):
		if 'user' in request.session.keys():
			#TEMPORARY
			return render(request, "Profile/home.html")
		else:
			raise PermissionDenied("You cant access this page")
