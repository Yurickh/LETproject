#coding: utf-8

from abc import*

from ELO.models import Student

from django.shortcuts import render
from django import forms

## @package ProfileUnit
# Este arquivo é responsável pelo armazenamento de todas as camadas correspondentes ao 
# módulo de perfil. Os métodos aqui são criados e chamados pela Factory (MainUnit.py) quando necessários. Eles são responsáveis pelo 
# redirecionamento do usuário para páginas diferentes dependendo do tipo de usuário, edição de dados pessoais, visualização de informações
# relativas aos cursos.

## Interface para a camada de Apresentação de Usuário do módulo Profile.
# É responsável pelo carregamento do template correto e processa os dados inseridos nos formulários de Perfil.
class IfUiProfile:
	__metaclass__ = ABCMeta

	## Força a criação da camada subjacente.
	def __init__(self, bus):
		try:
			self.bus = bus
		except TypeError as exc:
			del self
			raise exc

	@property
	def bus(self):
		return self.__bus

	@bus.setter
	def bus(self, value):
		if isinstance(value, IfBusProfile):
			self.__bus = value
		else:
			raise TypeError("Expected IfBusProfile instance at UiProfile.__bus. Received " + str(type(value)) + " instead.")

	@bus.deleter
	def bus(self):
		del self.__bus

	## 'Run' é o principal método de qualquer classe de apresentação. Este método permite a Factory dar o controle do programa à este módulo.
	@abstractmethod
	def run(self, request): pass


## Interface para a camada de Negócio do módulo de perfil. É responsável por...
class IfBusProfile:
	__metaclass__ = ABCMeta

	## Força a criação das camadas subjacentes.
	def __init__(self, pers):
		try:
			self.pers = pers
		except TypeError as exc:
			del self
			raise exc

	@property
	def pers(self):
		return self.__pers
	
	@pers.setter
	def pers(self, value):
		if isinstance(value, IfPersProfile):
			self.__pers = value
		else:
			raise TypeError("Expected IfPersProfile instance at BusProfile.__pers. Received " + str(type(value)) + "instead.")

	@pers.deleter
	def pers(self):
		del self.__pers

	@abstractmethod
	def refreshUser(self, user)


class IfPersProfile:
	__metaclass__ = ABCMeta

	@abstractmethod
	def fetch(self, user): pass

class UiProfileS(IfUiProfile): 

	def run(self, request):
		if not 'avatar' in user:
		self.bus.refreshUser(request.session['user'])
		return render(request, "Profile/home.html", {'user' : user})

class BusProfileS(IfBusProfile):

	def refreshUser(self, user):
		user = dict(user.items() + self.pers.fetch(user['name']))

class PersProfileS(IfPersProfile):

	def fetch(self, username):

		try:
			uid = Student.objects.get(field='NAME', value=username)['identity']

			fetchset = [
				('password', Student.objects.get(identity=uid, field='PASSWORD')
			]
		except Student.doesNotExist as exc:
			return []

class UiProfileP(IfUiProfile): 

	def run(self, request):
		return render(request, "Profile/home.html")


class BusProfileP(IfBusProfile): pass

class PersProfileP(IfPersProfile): pass
