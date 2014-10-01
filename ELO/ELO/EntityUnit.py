#coding: utf-8

## @package EntityUnit
#	Arquivo contem as entidades do programa.
#	Aqui encontra-se todo o código referentes as estruturas das entidades do
#   	programa.
#	Entidades não posseuem métodos alêm de:'set', 'get' e 'del' para definir, 
#	acessar e deletar suas propriedades. 

from BaseUnit import *
from abc import *

import ELO.locale.index as lang

## Definição das interfaces para classes de usuários.
#	Inclui-se 'name' e 'password', propriedades concretas que serão
#	passadas áquelas que delas derivam.
#	Perceba  que um objeto 'User' nao pode ser instanciado e para que uma 
#	classe derivada seja instaciada, ela deve sobrepor a propriedade
#	abstrata _User__instantiable.	
class User:
	
	
	## Especifica que uma classe é uma abstrata. Por isso, ela há de ser instanciada.
	#
	__metaclass__ = ABCMeta

	# Garante que um 'User' Jamais será criado. """
	__instantiable = abstractproperty()

	@property
	def name(self):
		return self._name

	@property
	def password(self):
		return self._password

	@property
	def lastLogin(self):
		return self._lastLogin

	@name.setter
	def name(self, value):
		if type(value) is Name:
			self._name = value
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_USR_NM'])

	@password.setter
	def password(self, password):
		if type(password) is Password:
			self._password = password
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_USR_PW'])

	@lastLogin.setter
	def lastLogin(self, value):
		if type(value) is Date:
			self._lastLogin = value
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_USR_DT'])

	@name.deleter
	def name(self):
		del self._name

	@password.deleter
	def password(self):
		del self._password

	@lastLogin.deleter
	def lastLogin(self):
		del self._lastLogin

## Administrador do sistema.
#	Eles controlam os processos e o fluxo dos procedimentos no programa.
#	Eles são os únicos com permissões para criar e deletar cursos. Entretanto
#	não possuem permissão para modificar cursos já criados. Ou seja, não têm 
#	permissão para interferir no desenvolvimento dos cursos.
class Adm(User):
	
	_User__instantiable = True

	def __init__(self, name, password, language):
		try:
			self.name = name
			self.password = password
			self.language = language
		except ValueError as exc:
			del self
			raise exc
		
	@property
	def language(self):
		return self.__language

	@language.setter
	def language(self, language):
		if type(language) is Language:
			self.__language = language
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_STU_LN'])

	@language.deleter
	def language():
		del __language

## Representação do Professor para o sistema.
#Refere-se tanto a professores de fato, quanto a monitores.
#Eles tem permição para montar cursos e modificar cursos.
#Vale ressaltar que o professor NÃO pode criar cursos, apenas monta-los a partir
#
class Professor(User):
	_User__instantiable = True

	def __init__(self, name, password, matric, bios, campus, courses, avatar, sex):
		try:
			self.name = name
			self.password = password
			self.matric = matric
			self.bios = bios
			self.campus = campus
			self.courses = courses
			self.avatar = avatar
			self.sex = sex
			self.email = email
		except ValueError as exc:
			del self
			raise exc
	@property
	def email(self):
		return self.__email
	@email.setter
	def email(self, value):
		if type(value) is Mail:
			self.__email = value 
		else :
			raise ValueError(lang.DICT['EXCEPTION_INV_PRF_ML'])
	@property
	def matric(self):
		return self.__matric

	@matric.setter
	def matric(self, value):
		if type(value) is Matric:
			self.__matric = value
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_PRF_MT'])
	@matric.deleter
	def matric(self):
		del self.__matric


	@property
	def bios(self):
		return self.__bios

	@bios.setter
	def bios(self, bios):
		if type(bios) is PlainText:
			self.__bios = bios
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_PRF_BS'])

	@bios.deleter
	def bios(self):
		del self.__bios


	@property
	def campus(self):
		return self.__campus

	@campus.setter
	def campus(self, campus):
		if type(campus) is Campus:
			self.__campus = campus
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_PRF_CP'])

	@campus.deleter
	def campus(self):
		del self.__campus


	@property
	def courses(self):
		return self.__courses

	@courses.setter
	def courses(self, courses):
		if type(courses) is list and (type(courses[0]) is Id or not courses):
			self.__courses = courses
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_PRF_CS'])

	@courses.deleter
	def courses(self):
		del self.__courses


	@property
	def avatar(self):
		return self.__avatar

	@avatar.setter
	def avatar(self, avatar):
		if type(avatar) is Link:
			self.__avatar = avatar
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_PRF_AV'])

	@avatar.deleter
	def avatar(self):
		del self.__avatar


	@property
	def sex(self):
		return self.__sex

	@sex.setter
	def sex(self, sex):
		if type(sex) is Sex:
			self.__sex = sex
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_PRF_SX'])

	@sex.deleter
	def sex(self):
		del self.__sex


##Por ultimo, mas não menos importante, o aluno.
#Principal usuário desse software.
#Alunos tem permição para atender a cursos e  resolver exercícios.
class Student(User):
	
	_User__instantiable = True

	def __init__(self, name, password, matric, bios, campus, courses, avatar, email, sex, grades, interests, language):
		try:
			self.name = name
			self.password = password
			self.matric = matric
			self.bios = bios
			self.campus = campus
			self.courses = courses
			self.avatar = avatar
			self.email = email
			self.sex = sex
			self.grades = grades
			self.interests = interests
			self.language = language
		except ValueError as exc:
			del self
			raise exc

	@property
	def matric(self):
		return self.__matric

	@matric.setter
	def matric(self, matric):
		if type(matric) is Matric:
			self.__matric = matric
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_STU_MT'])

	@matric.deleter
	def matric(self):
		del __matric


	@property	
	def bios(self):
		return self.__bios

	@bios.setter
	def bios(self, bios):
		if type(bios) is PlainText:
			self.__bios = bios
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_STU_BS'])

	@bios.deleter
	def bios(self):
		del __bios


	@property
	def campus(self):
		return self.__campus

	@campus.setter
	def campus(self, campus):
		if type(campus) is Campus:
			self.__campus = campus
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_STU_CP'])

	@campus.deleter
	def campus(self):
		del __campus


	@property
	def courses(self):
		return self.__courses

	@courses.setter
	def courses(self, courses):
		if (type(courses[0]) is Id or not courses) and type(courses) is list :
			self.__courses = courses
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_STU_CO'])

	@courses.deleter
	def courses(self):
		del __courses


	@property
	def avatar(self):
		return self.__avatar

	@avatar.setter
	def avatar(self, avatar):
		if type(avatar) is Link:
			self.__avatar = avatar
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_STU_AV'])

	@avatar.deleter
	def avatar(self):
		del __avatar


	@property
	def sex(self):
		return self.__sex

	@sex.setter
	def sex(self, sex):
		if type(sex) is Sex:
			self.__sex = sex
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_STU_SX'])

	@sex.deleter
	def sex(self):
		del __sex


	@property
	def email(self):
		return self.__email

	@email.setter
	def email(self, email):
		if type(email) is Mail:
			self.__email = email
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_STU_ML'])

	@email.deleter
	def email(self):
		del __email


	@property
	def grades(self):
		return self.__grades

	@grades.setter
	def grades(self, grades):
		if type(grades) is dict and type(grades.values()[0]) is Grades:
			self.__grades = grades
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_STU_GR'])

	@grades.deleter
	def grades(self):
		del __grades


	@property
	def interests(self):
		return self.__interests

	@interests.setter
	def interests(self, interests):
		if type(interests) is PlainText:
			self.__interests = interests
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_STU_IN'])

	@interests.deleter
	def interests(self):
		del __interests


	@property
	def language(self):
		return self.__language

	@language.setter
	def language(self, language):
		if type(language) is Language:
			self.__language = language
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_STU_LN'])

	@language.deleter
	def language():
		del __language


## Um curos possui módulos, que por sua vez, contêm lições, e estas possuem
#exercícios. "Courses" estão em um nivel mais alto do sistema de abstração.
#Normalmente, a um professor será dado cursos vazios, e a partir destes 
#ele poderá criar sua dinámica letiva.
class Courses(object):

	def __init__(self, name, thisId, students, modules):
		try:
			self.name = name
			self.thisId = thisId
			self.students = students
			self.modules = modules
		except ValueError as exc:
			del self
			raise exc


	@property		
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		if type(name) is Name:
			self.__name = name
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_CRS_NM'])

	@property
	def thisId(self):
		return self.__thisId

	@thisId.setter
	def thisId(self, thisId):
		if type(thisId) is Id:
			self.__thisId = thisId
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_CRS_ID'])

	@property
	def students(self):
		return self.__students

	@students.setter
	def students(self, students):
		if type(students) is list and (type(students[0]) is Id or not students):
			self.__students = students
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_CRS_ST'])

	@property
	def modules(self):
		return self.__modules		

	@modules.setter
	def modules(self, modules):
		if type(modules) is list and (type(modules[0]) is Id or not modules):
			self.__modules = modules
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_CRS_MD'])

	@name.deleter
	def name(self):
		del __name

	@thisId.deleter
	def thisId(self):
		del __thisId

	@students.deleter
	def students(self):
		del __students

	@modules.deleter
	def modules(self):
		del __modules

## Módulos contêm lições.
#São camadas intermediárias de abstração entre cursos e lições.
#A conclusão de um módulo possibilita o engeço no seguinte. Como níveis em um 
#jogo. 
class Module(object):
	def __init__(self, name, thisId, lessons):
		try:
			self.name = name
			self.thisId = thisId
			self.lessons = lessons
		except ValueError as exc:
			del self
			raise exc

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		if type(name) is Name:
			self.__name = name
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_MD_NM'])

	@name.deleter
	def name(self):
		del self.__name


	@property
	def thisId(self):
		return self.__thisId

	@thisId.setter
	def thisId(self, thisId):
		if type(thisId) is Id:
			self.__thisId = thisId
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_MD_ID'])

	@thisId.deleter
	def thisId(self, thisId):
		del self.__thisId


	@property
	def lessons(self):
		return self.__lessons

	@lessons.setter
	def lessons(self, lessons):
		if type(lessons) is list and (type(lessons[0]) is Id or not lessons):
			self.__lessons = lessons
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_MD_LT'])

	@lessons.deleter
	def lessons(self):
		del self.__lessons

##Compõe a camada mais baixa de abstração do sistema
#Lições são amplamente adaptáveis e customisáveis. Podem assumir o fotmato que 
#o professor desejar. Para isso deve-se lincar o Link do conteúdo a desejado.
#Lições sempre contêm pelo menos 1 exercício.
class Lesson(object):

	def __init__(self, name, thisId, link, exercises):
		try:
			self.name = name
			self.thisId = thisId
			self.link = link
			self.exercises = exercises
		except ValueError as exc:
			del self
			raise exc

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		if type(name) is Name:
			self.__name = name
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_LS_NM'])

	@name.deleter
	def name(self):
		del self.__name

	@property
	def thisId(self):
		return self.__thisId

	@thisId.setter
	def thisId(self, thisId):
		if type(thisId) is Id:
			self.__thisId = thisId
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_LS_ID'])

	@thisId.deleter
	def thisId(self):
		del self.__thisId

	@property
	def link(self):
		return self.__link

	@link.setter
	def link(self, link):
		if type(link) is Link:
			self.__link = link
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_LS_LK'])

	@link.deleter
	def link(self):
		del self.__link

	@property
	def exercises(self):
		return self.__exercises

	@exercises.setter
	def exercises(self, exercises):
		if type(exercises) is list and (type(exercises[0]) is Id or not exercises):
			self.__exercises = exercises
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_LS_ST'])

	@exercises.deleter
	def exercises(self):
		del self.__exercises

##Unidade básica de apresendisado. 
#Em cada lição haverão exercicios com o intuito de avaliar o desenpenho do aluno.
#O rendimento do aluno em tais exercicios regerá a experiência do aluno no curos
class Exercise(object):

	def __init__(self, thisId, link, exType, exFormat, items):
		try:
			self.thisId = thisId
			self.link = link
			self.exType = exType
			self.exFormat = exFormat
			self.items = items
		except ValueError as exc:
			del self
			raise exc


	@property
	def thisId(self):
		return self.__thisId

	@thisId.setter
	def thisId(self, thisId):
		if type(thisId) is Id:
			self.__thisId = thisId
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_EX_ID'])

	@thisId.deleter
	def thisId(self):
		del self.__thisId

	@property
	def link(self):
		return self.__link

	@link.setter
	def link(self, link):
		if type(link) is Link:
			self.__link = link
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_EX_LK'])

	@link.deleter
	def link(self):
		del self.__link

	@property
	def exType(self):
		return self.__exType

	@exType.setter
	def exType(self, exType):
		if type(exType) is ExType:
			self.__exType = exType
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_EX_ET'])

	@exType.deleter
	def exType(self):
		del self.__exType

	@property
	def exFormat(self):
		return self.__exFormat

	@exFormat.setter
	def exFormat(self, exFormat):
		if type(exFormat) is Id:
			self.__exFormat = exFormat
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_EX_FT'])

	@exFormat.deleter
	def exFormat(self):
		del self.__exFormat

	@property
	def items(self):
		return self.__items

	@items.setter
	def items(self, items):
		if type(items) is list and (type(items[0]) is Id or not items):
			self.__items = items
		else:
			raise ValueError(lang.DICT['EXCEPTION_INV_EX_IT'])

	@items.deleter
	def items(self):
		del self.__items

#.
