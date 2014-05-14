#coding: utf-8

## @file MainUnit.py
#	Arquivo responsável pela devida execução e estruturação do programa.
#
#	Aqui reside a Factory, a classe que deve montar a estrutura do resto
#	do programa, para que ele execute da forma correta, bem como outros
#	blocos fundamentais para o funcionamento do sistema como um todo.

from abc import *
from importlib import import_module

from Login.LoginUnit import *
from Profile.ProfileUnit import *
from Adm.AdmUnit import *
from Course.CourseUnit import *

from models import Adm, Professor, Student

from django.core.exceptions import PermissionDenied
from django.http import Http404

## @if Verifica qual a linguagem selecionada para renderizar os templates.
if 'LANG' in globals():
	if LANG == 'en_us':
		lang = import_module("ELO.lang.en_us")
	else:
		lang = import_module("ELO.lang.pt_br")
else:
	lang = import_module("ELO.lang.pt_br")


## Insere os objetos user e DICT em todas as renderizações de template.
def globalContext(request):
	return {
			'user': request.session['user'] if ('user' 
				in request.session.keys()) else False,
			'DICT': lang.DICT,
		}

## Classe factory.
# 	Responsável pela construção e controle de fluxo de todo o programa. 
# 	Tudo é criado a partir dela.
class Factory:
	__ui = None
	__bus = None
	__pers = None

	## Classe que executa o módulo de login.
	# 	Define as camadas de persistência, negócio de login e
	#	apresentação e verifica o tipo de usuário.
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
	# 	Finaliza a sessão do usuário e redireciona para 
	#	a página de login.
	def runLogout(self, request):
		if 'user' in request.session.keys():
			del request.session['user']
		return self.runLogin(request, "Student")

	## Classe que executa o módulo de Perfil.
	# 	Define as camadas de persistência, negócio e apresentação de
	#	perfil e proíbe o acesso de usuários não logados no sistema.
	def runProfile(self, request):
		if 'user' in request.session.keys():
			if request.session['user']['type'] == 'Adm':
				return self.runAdm(request)
			elif request.session['user']['type'] == 'Professor' or request.session['user']['type'] == 'Student':
				if not isinstance(self.__ui, IfUiProfile):
					self.__pers = PersProfile()
					self.__bus = BusProfile(self.__pers)
					self.__ui = UiProfile(self.__bus)
				return self.__ui.run(request)
			else:
				raise Http404(DICT["EXCEPTION_404_ERR"])
		else:
			raise PermissionDenied(DICT["EXCEPTION_403_STD"])

	## Classe que executa o módulo de Administração.
	# 	Define as camadas de persinstência, negócio e apresentação de
	#	administração.
	def runAdm(self, request):
		if 'user' in request.session.keys():
			if request.session['user']['type'] == 'Adm':
				if not isinstance(self.__ui, IfUiAdm):
					self.__pers = PersAdm()
					self.__bus = BusAdm(self.__pers)
					self.__ui = UiAdm(self.__bus) 
				return self.__ui.run(request)
		
		raise PermissionDenied(DICT["EXCEPTION_403_STD"])

	## Classe que executa o módulo de Curso.
	# 	Define as camdas de persistência, negócio e apresentação de
	#	curso.
	def runCourse(self, request):
		if 'user' in request.session.keys():
			if not self.__ui is IfUiCourse:
				self.__per = PersAdm()
				self.__bus = BusAdm(self.__pers)
				self.__ui = UiAdm(self.__bus)

			return self.__ui.run(request)
