#coding: utf-8

from abc import*
from django.shortcuts import render

## @package AdmUnit
#Este arquivo é responsável pelo armazenamento de todas as camadas correspondentes ao módulo de administrador. Os métodos aqui são 
#criados e chamados pela Factory (MainUnit.py) quando necessários. São responsáveis por cadastrar, deletar e editar alunos e professores 
#no banco de dados, criar cursos e ver um log sobre os últimos eventos no sistema.


## Interface para a camada de apresentação de Usuário do módulo de Administração.
# É responsável por...
class IfUiAdm:
	__metaclass__ = ABCMeta
	
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
		if isinstance(value, IfBusAdm):
			self.__bus = value
		else:
			raise TypeError("Expected IfBusAdm instance at UiAdm.__bus. Received " + str(type(value)) + " instead.")

	@bus.deleter
	def bus(self):
		del self.__bus

	@abstractmethod
	def run(self, request): pass

## Interface para a camada de negócio do módulo de perfil.
# É responsável por...
class IfBusAdm:
	__metaclass__ = ABCMeta

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
		if isinstance(value, IfPersAdm):
			self.__pers = value
		else:
			raise TypeError("Expected IfPersAdm instance at BusAdm.__pers. Received " + str(type(value)) + " instead.")

	@pers.deleter	
	def pers(self):
		del self.__pers

## Interface para a camada de persistência do módulo de administração.
# É responsável por...
class IfPersAdm:	pass

## Camada de interface de usuário para o módulo de administração.
class UiAdm(IfUiAdm):

	def run(self, request):
		return render(request, "Adm/home.html")

## Camada de negócio para o módulo de administração.
class BusAdm(IfBusAdm):	pass

## Camada de persistência para o módulo de administração.
class PersAdm(IfPersAdm): pass



