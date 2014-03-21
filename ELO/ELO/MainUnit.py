#coding: utf-8
##@package MainUnit
#Parte inicial responsavel por construir e executar o sistema.

from abc import *

from Login.LoginUnit import *
from Profile.ProfileUnit import *
from Adm.AdmUnit import *
from Course.CourseUnit import *

from models import Adm, Professor, Student

from django.core.exceptions import PermissionDenied
from django.http import Http404

import importlib

if 'LANG' in globals():
	if LANG == 'en_us':
		importlib.import_module("ELO.lang.en_us")
	else:
		importlib.import_module("ELO.lang.pt_br")
else:
	importlib.import_module("ELO.lang.pt_br")


def globalContext(request):
	return {
			'user': request.session['user'] if ('user' in request.session.keys()) else False,
			'DICT': DICT,
		}

## Classe factory.
# Responsável pela construção e controle de fluxo de todo o programa. Tudo é criado a partir dela.
class Factory:
	__ui = None
	__bus = None
	__pers = None

	## Classe que executa o módulo de login.
	# Define as camadas de persistência, negócio de login e apresentação e verifica o tipo de usuário.
	def runLogin(self, request, entity):
		if not isinstance(self.__ui, IfUiLogin):
			self.__pers = PersLogin()
			self.__bus = BusLogin(self.__pers)
			self.__ui = UiLogin(self.__bus)

		if entity == "Adm":
			database = Adm
		elif entity == "Professor":
			database = Professor
		elif entity == "Student":
			database = Student
		else:
			database = None

		return self.__ui.run(request, database)

	## Classe que executa o logout.
	# Finaliza a sessão do usuário e redireciona para a página de login.
	def runLogout(self, request):
		if 'user' in request.session.keys():
			del request.session['user']
		return self.runLogin(request, "Student")

	## Classe que executa o módulo de Perfil.
	# Define as camadas de persistência, negócio e apresentação de perfil e proíbe o acesso de usuários não logados no sistema.
	def runProfile(self, request):
		if 'user' in request.session.keys():
			if request.session['user']['type'] == 'Adm':
				self.runAdm(request)
			elif request.session['user']['type'] == 'Professor':
				if not isinstance(self.__ui, IfUiProfile):
					self.__pers = PersProfileP()
					self.__bus = BusProfileP(self.__pers)
					self.__ui = UiProfileP(self.__bus)
				return self.__ui.run(request)
			elif request.session['user']['type'] == 'Student':
				if not isinstance(self.__ui, IfUiProfile):
					self.__pers = PersProfileS()
					self.__bus = BusProfileS(self.__pers)
					self.__ui = UiProfileS(self.__bus)
				return self.__ui.run(request)
			else:
				raise Http404(DICT["EXCEPTION_404_ERR"])
		else:
			raise PermissionDenied(DICT["EXCEPTION_403_STD"])

	## Classe que executa o módulo de Administração.
	# Define as camadas de persinstência, negócio e apresentação de administração.
	def runAdm(self, request):
		if 'user' in request.session.keys():
			if request.session['user']['type'] == 'Adm':
				if not self.__ui is IfUiAdm:
					self.__pers = PersProfile()
					self.__bus = BusAdm(self.__pers)
					self.__ui = UiAdm(self.__bus) 
	
				return self.__ui.run(request)
		
		raise PermissionDenied(DICT["EXCEPTION_403_STD"])

	## Classe que executa o módulo de Curso.
	# Define as camdas de persistência, negócio e apresentação de curso.
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
