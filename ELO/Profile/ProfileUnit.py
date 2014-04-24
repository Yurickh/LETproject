#coding: utf-8

from abc import*

from ELO.models import Student

from django.shortcuts import render
from django import forms

## @file ProfileUnit.py
# 	Este arquivo é responsável pelo armazenamento de todas as camadas 
# correspondentes ao módulo de perfil. 
#	Os métodos aqui são criados e chamados pela Factory (MainUnit.py)
# quando necessários. Eles são responsáveis pelo redirecionamento do usuário
# para páginas diferentes dependendo do tipo de usuário, edição de dados 
# pessoais, visualização de informações relativas aos cursos.

## Interface para a camada de Apresentação de Usuário do módulo Profile.
# 	É responsável pelo carregamento do template correto e processa os 
# 	dados inseridos nos formulários de Perfil.
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
			raise TypeError("Expected IfBusProfile instance at \
				UiProfile.__bus. Received " + 
				str(type(value)) + " instead.")

	@bus.deleter
	def bus(self):
		del self.__bus

	## 'Run' é o principal método de qualquer classe de apresentação. 
	# 	Este método permite a Factory dar o controle do programa 
	# 	módulo.
	@abstractmethod
	def run(self, request): pass


## Interface para a camada de Negócio do módulo de perfil.
#	É responsável por executar a atualização do Cookie de dados do
#	usuário, bem como a devida recuperação de dados para o sistema.
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
			raise TypeError("Expected IfPersProfile instance at \
				BusProfile.__pers. Received " + 
				str(type(value)) + "instead.")

	@pers.deleter
	def pers(self):
		del self.__pers

	@abstractmethod
	def refreshUser(self, user): pass


## Interface para a camada de Persistência do módulo de perfil.
#	É responsável pela recuperação dos dados do usuário logado do banco
#	de dados.
class IfPersProfile:
	__metaclass__ = ABCMeta

	@abstractmethod
	def fetch(self, user): pass

## Camada de apresentação para estudantes.
#	Deve carregar o devido template, contendo os dados básicos do estudante
#	bem como os cursos matriculados e seu histórico.
class UiProfileS(IfUiProfile): 

	def run(self, request):
		user = request.session['user']
		if not 'avatar' in user:
			request.session['user'] = self.bus.refreshUser(user)
			user = request.session['user']
		return render(request, "Profile/home.html", {'user' : user})

## Camada de negócio para estudantes.
#	Deve ser capaz de gerar um dicionário contendo uma versão mais nova
#	dos dados do usuário.
class BusProfile(IfBusProfile):

	def refreshUser(self, user):
		if user['type'] == 'Student':
			return dict(user.items()+ self.pers.fetch(user['name'], Student))
		elif user['type'] == 'Professor':
			return dict(user.items()+ self.pers.fetch(user['name'], Professor))

## Camada de persistência para estudantes.
#	Recupera os dados do estudante logado, retornando-os para a camada
#	de negócio.
class PersProfile(IfPersProfile):

	def __select_field(self, uid, field, database):

		try:
			ret = database.objects.get(identity=uid, field=field)
			ret = ret.value

		except database.MultipleObjectsReturned:
			ret = map(lambda x: x.value, Student.objects.filter(
					identity=uid, field=field))

		except Student.DoesNotExist:
			ret = None

		return ret

	def fetch(self, username, database):

		try:
			uid = database.objects.get(field='NAME', value=username)
			uid = uid.identity

			sf = lambda x: self.__select_field(uid, x, database)

			fetchset = [
					('password',	sf('PASSWORD')),
					('matric',		sf('MATRIC')),
					('bios',		sf('BIOS')),
					('campus',		sf('CAMPUS')),
					('courses',		sf('COURSE')),
					('avatar',		sf('AVATAR')),
					('email',		sf('EMAIL')),
					('sex',			sf('SEX')),
			]

			if database is Student:
				fetchset = fetchset + [		
					('grades',		sf('GRADE')),
					('interests',	sf('INTEREST')),
					('language',	sf('LANGUAGE')),
				]

		except database.DoesNotExist as exc:
			fetchset = []

		return fetchset

class UiProfileP(IfUiProfile): 

	def run(self, request):
		return render(request, "Profile/home.html")
