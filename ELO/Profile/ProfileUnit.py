#coding: utf-8

from abc import*
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


class IfPersProfile:

	## Retorna 
	def select(self, username, database): pass

	def update(self, 

class UiProfileS(IfUiProfile): 

	def run(self, request):
		

class BusProfileS(IfBusProfile): pass

class PersProfileS(IfPersProfile): pass

class UiProfileP(IfUiProfile): pass

class BusProfileP(IfBusProfile): pass

class PersProfileP(IfPersProfile): pass
