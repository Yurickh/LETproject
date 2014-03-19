#coding: utf-8

## Este arquivo é responsável pelo armazenamento de todas as camadas correspondentes ao módulo de login.
# Os métodos aqui são criados e chamados pela Factory (MainUnit.py) quando necessários.
# Eles são responsáveis pela criação, gestão e deleção do objeto de sessão e a validação e login dos usuários.

from abc import *

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import Template, Context
from django import forms

from ELO.models import Student, Adm, Professor
from ELO.BaseUnit import Name, Password
from Login.forms import LoginForm
from ELO.lang.pt_br import *

## Interface para a camada de Apresentação de Usuário do módulo Login.
# É responsável pelo carregamento do template correto e processa os dados inseridos no formulário de login.
class IfUiLogin:
	## Força a criação da camada subjacente
	__metaclass__ = ABCMeta

	def __init__(self, bus):
		try:
			self.bus = bus
		except TypeError as exc:
			del self
			raise exc

	@property
	## Camada de negócio associada à camada de UI (user interface). Essas camadas estão ligadas pelo módulo de MainUnit.
	def bus(self):
		return self.__bus

	@bus.setter
	def bus(self, value):
		if isinstance(value, IfBusLogin):
			self.__bus = value
		else:
			raise TypeError("Expected IfBusLogin instance at UiLogin.__bus. Received " + str(type(value)) + " instead.")

	## Método de deleção do objeto que representa a camada de negócio.
	@bus.deleter
	def bus(self):
		del self.__bus

	## O método principal de qualquer classe de UI (user interface), o método run() permite a Factory dar o controle do programa a dado 
	# módulo.
	@abstractmethod
	def run(self, request): pass


## Interface para a camada de negócio do módulo de Login.
# Responsável pela validação dos dados submetidos através do formulário de login.
class IfBusLogin: 
	__metaclas__ = ABCMeta

	## Método de validação não retorna nada, mas lança uma excessão se a validação não for bem sucedida.
	@abstractmethod
	def validate(self, username, password): pass

	@property
	def pers(self):
		return self.__pers

	@pers.setter
	def pers(self, pers):
		if isinstance(value, IfPersLogin):
			self.__pers = pers
		else:
			raise TypeError("Expected IfPersLogin instance at BusLogin.__pers. Received " + str(type(value)) + "instead.")

	## Método de deleção do objeto que representa a camada de persistência.
	@pers.deleter
	def pers(self):
		del self.__pers

	## Força a criação da camada subjacente.
	def __init__(self, value):
		try:
			self.pers = value
		except TypeError as exc:
			del self
			raise exc


## Interface para a camada de persistência do módulo de Login.
class IfPersLogin:

	__metaclass__ = ABCMeta

	@abstractmethod
	def select(self, username, database): pass


## Camada de interface de usuário para o módulo de Login.
class UiLogin(IfUiLogin):

	## Método que inicia o módulo de login. Aqui, ocorre a validação de formulário, autenticação de usuário, e redirecionamento apra a
	# página de perfil.
	def run(self, request, database):
		if request.method == "POST":
			login_form = LoginForm(request.POST)
			try: 
				if login_form.is_valid():
					self.bus.validate(login_form.cleaned_data['username'], login_form.cleaned_data['password'], database)
				else:
					raise ValueError("Login ou senha incorretos.")
			except ValueError as exc:
				if database.__name__ == "Professor":
					target = "proflogin"
				elif database.__name__ == "Adm":
					target = "364fd8cdc3a35a89b7be75bc9d10ebea"
				else:
					target = ""

				return render(request, "Login/form.html", {'form': login_form, 'error': exc, 'target': target})
			else:
				request.session['user'] = {
								'name': login_form.cleaned_data['username'].value,
								'password': login_form.cleaned_data['password'].value,
								'type': database.__name__,
							}
				return HttpResponseRedirect('/profile')
		else:
			login_form = LoginForm()

			if not database:
				target = ""
			if database.__name__ == "Professor":
				target = "proflogin"
			elif database.__name__ == "Adm":
				target = "364fd8cdc3a35a89b7be75bc9d10ebea"
			else:
				target = ""

			return render(request, "Login/form.html", {'form': login_form, 'target': target})


## Camada de negócio de usuário para o módulo de Login.
class BusLogin(IfBusLogin):

	## Método de validação do username e password. Ele recebe da camada de persistência os valores correspondentes ao username e password e 
	# verifica com o inserido pelo usuário.
	def validate(self, username, password, database):
		upass = self.pers.select(username.value, database)
		if not upass or upass['password'] != password.value:
			raise ValueError(EXCEPTION_INV_LOG)

## Camada de persistência de usuário para o módulo de Login.
class PersLogin(IfPersLogin):

	## Método de busca no banco de dados. Recebe o nome de usuário e busca no bando de dados o valor correspondente à senha daquele usuário.
	def select(self, username=None, database=None):
		if not username: return False
		if not database: return False

		try:
			uid = database.objects.get(value=username, field='NAME').identity
			upass = database.objects.get(identity=uid, field='PASSWORD').value
			return {'name': username, 'password': upass}
		except database.DoesNotExist:
			return False
		
