#coding: utf-8

from abc import *
from Login.LoginUnit import *
from Profile.ProfileUnit import *
from Adm.AdmUnit import *
from Course.CourseUnit import *

from Login.models import Adm, Professor, Student

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

	def runLogin(self, request, entity):
		if not isinstance(self.__ui, IfUiLogin):
			self.__pers = PersLogin()
			self.__bus = BusLogin(self.__pers)
			self.__ui = UiLogin(self.__bus)

		if entity == "Adm":
			database = models.Adm
		elif entity == "Professor":
			database = models.Professor
		elif entity == "Student":
			database = models.Student

		return self.__ui.run(request, database)

	def runLogout(self, request):
		if 'user' in request.session.keys():
			del request.session['user']
		return self.runLogin(request)


	def runProfile(self, request):
		if 'user' in request.session.keys():
			if not isinstance(self.__ui, IfUiProfile):
				self.__pers = PersProfile()
				self.__bus = BusProfile(self.__pers)
				self.__ui = UiProfile(self.__bus)
			return self.__ui.run(request)
		else:
			raise PermissionDenied("You cannot access this page :p")


	def runAdm(self, request):
		if 'user' in request.session.keys():
			if not self.__ui is IfUiAdm:
				self.__pers = PersProfile()
				self.__bus = BusAdm(self.__pers)
				self.__ui = UiAdm(self.__bus) 

			return self.__ui.run(request)


	def runCourse(self, request):
		if 'user' in request.session.keys():
			if not self.__ui is IfUiCourse:
				self.__per = PersAdm()
				self.__bus = BusAdm(self.__pers)
				self.__ui = UiAdm(self.__bus)

			return self.__ui.run(request)

"""
	def runBuilding(self, request):
"""
