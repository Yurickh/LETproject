#coding: utf-8

## @file MainUnit.py
#	Arquivo responsável pela devida execução e estruturação do programa.
#
#	Aqui reside a Factory, a classe que deve montar a estrutura do resto
#	do programa, para que ele execute da forma correta, bem como outros
#	blocos fundamentais para o funcionamento do sistema como um todo.

from abc import *

from Login.LoginUnit import *
from Profile.ProfileUnit import *
from Adm.AdmUnit import *
from Course.CourseUnit import *

import ELO.locale.index as lang

from models import Adm, Professor, Student, God

from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.utils import translation

## Insere os objetos user e DICT em todas as renderizações de template.
def globalContext(request):
	_sess = request.session
	return {
			'user': _sess['user'] if ('user' in _sess.keys()) else False,
			'DICT': lang.DICT,
		}

## Classe factory.
#	Responsável pela construção e controle de fluxo de todo o programa. 
# 	Tudo é criado a partir dela.
class Factory:
	__ui = None
	__bus = None
	__pers = None

	## Classe que redireciona para a devida home.
	#	Caso o usuário já esteja devidamente logado, redireciona para o
	#	profile, caso contrário, vai para a página de login.
	@method_decorator(vary_on_cookie)
	@method_decorator(csrf_protect)
	def runHome(self, request, entity):
		if 'user' in request.session.keys():
			if (request.session['user']['type'] == "Adm" or 
			   request.session['user']['type'] == "God"):
				return self.runAdm(request)
			else:
				return self.runProfile(request, acctype='Home')
		else:
			return self.runLogin(request, entity)

	## Classe que executa o módulo de login.
	# 	Define as camadas de persistência, negócio de login e
	#	apresentação e verifica o tipo de usuário.
	@method_decorator(vary_on_cookie)
	@method_decorator(csrf_protect)
	def runLogin(self, request, entity):
		if not isinstance(self.__ui, IfUiLogin):
			self.__pers = PersLogin()
			self.__bus = BusLogin(self.__pers)
			self.__ui = UiLogin(self.__bus)

		if entity == "Adm":
			database = Adm
 		elif entity == "God":
			database = God
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
			del request.session[translation.LANGUAGE_SESSION_KEY]
		return self.runLogin(request, "Student")

	## Classe que executa a página inicial do módulo de Perfil.
	# 	Define as camadas de persistência, negócio e apresentação de
	#	perfil e proíbe o acesso de usuários não logados no sistema.
	#
	#	@arg acctype 	Define o tipo de acesso que o usuário está requerindo.
	#					"Full": Acessa o Perfil completo, com possibilidade de
	#						edição. Caso a chamada seja assíncrona, retorna a
	#						form de edição do campo específico.
	#					"Home": Acessa o Perfil resumido, a home do site em si.
	@method_decorator(vary_on_cookie)
	@method_decorator(csrf_protect)
	def runProfile(self, request, acctype, field=None):
		if 'user' in request.session.keys(): # is user logged?
			user_type = request.session['user']['type']
			if user_type == 'Professor' or user_type == 'Student':
				if not isinstance(self.__ui, IfUiProfile):
					self.__pers = PersProfile()
					self.__bus = BusProfile(self.__pers)
				if acctype == "Full":
					self.__ui = UiFullProfile(self.__bus)
				elif acctype == "Home":
					self.__ui = UiHomeProfile(self.__bus)
				else:
					raise Http404(lang.DICT["EXCEPTION_404_ERR"])
			
				if field and acctype == "Full":
					return self.__ui.run(request, field)
				else:
					return self.__ui.run(request)
			else:
				raise Http404(lang.DICT["EXCEPTION_404_ERR"])
		else:
			raise PermissionDenied(lang.DICT["EXCEPTION_403_STD"])
		

	## Classe que executa o módulo de Administração.
	# 	Define as camadas de persinstência, negócio e apresentação de
	#	administração.
	@method_decorator(vary_on_cookie)
	@method_decorator(csrf_protect)
	def runAdm(self, request, action=None, model=None):
		#	Checa se usuario ja esta logado.
		if 'user' in request.session.keys():
			#	Checa se usuário é um Administrador ou Super Administrador.
			if(request.session['user']['type'] == 'Adm' or
			   request.session['user']['type'] == 'God'):
				#	Cria as instâncias caso elas ainda não tenham sido criadas.
				if not isinstance(self.__ui, IfUiAdm):
					self.__pers = PersAdm()
					self.__bus = BusAdm(self.__pers)
					self.__ui = UiAdm(self.__bus) 		
				#	Passa a ação a ser efetuada e o devido modelo a ser
				#		alterado para a run da Factory de Adm.
				if action != None and model != None:
					return self.__ui.run(request, action, model)
				
				return self.__ui.run(request)
		#	Caso o  usuário não esteja logado ou não seja Administrador,
		#		é negada a continuação das requisições.
		raise PermissionDenied(lang.DICT["EXCEPTION_403_STD"])

	## Classe que executa o módulo de Curso.
	# 	Define as camadas de persistência, negócio e apresentação de
	#	curso.
	@method_decorator(vary_on_cookie)
	@method_decorator(csrf_protect)
	def runCourse(self, request, courseid=None):
		if 'user' in request.session.keys():
			if not self.__ui is IfUiCourse:
				self.__pers = PersCourse()
				self.__bus = BusCourse(self.__pers)
				self.__ui = UiCourse(self.__bus)

			return self.__ui.run(request, courseid)
		print 'runCourse(' +str(self)+','+str(request)+',courseid='+str(courseid)
		raise PermissionDenied(lang.DICT["EXCEPTION_403_STD"])
