#coding: utf-8

""" Here lies all the code regarding the structure of the entities of this program.
	Entities shall not have methods beside the basics set, get and del methods for their properties. This file have 666 lines propositally.
"""

from BaseUnit import *
from abc import *
from lang.pt_br import *

class User:
	""" Interface definition for user-like classes.
		It includes the 'name' and 'password' concrete properties that are passed to whoever derives from it. Note that a User object cannot be instantiated and in order to instantiate a derived class, it has to override the _User__instantiable abstract property.
	"""
	__metaclass__ = ABCMeta
	""" Specifies that this class is an abstract class. Thus, it shall not be instantiated. """

	__instantiable = abstractproperty()
	""" Guarantee that a User will never be created. """

	@property
	def name(self):
		return self._name

	@property
	def password(self):
		return self._password

	@name.setter
	def name(self, value):
		if type(value) is Name:
			self._name = value
		else:
			raise ValueError(EXCEPTION_INV_USR_NM)

	@password.setter
	def password(self, password):
		if type(password) is Password:
			self._password = password
		else:
			raise ValueError(EXCEPTION_INV_USR_PW)

	@name.deleter
	def name(self):
		del self._name

	@password.deleter
	def password(self):
		del self._password

class Adm(User):
	""" Administrator of the system.
		The Administrators are the bosses. They control the processes and the flow of things in the program. They're the only ones allowed to create and destroy courses at will, but they cannot change courses already created. They're like merciful gods that won't mess with mere mortal's affairs.
	"""
	_User__instantiable = True

	def __init__(self, name, password):
		try:
			self.name = name
			self.password = password
		except ValueError as exc:
			del self
			raise exc

class Professor(User):
	""" The representation of the Professor inside the system.
		The professors may be real professors or monitors. They have the power to build, change and modify courses.
	"""
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
		except ValueError as exc:
			del self
			raise exc
	
	@property
	def matric(self):
		return self.__matric

	@matric.setter
	def matric(self, value):
		if type(value) is Matric:
			self.__matric = value
		else:
			raise ValueError(EXCEPTION_INV_PRF_MT)
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
			raise ValueError(EXCEPTION_INV_PRF_BS)

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
			raise ValueError(EXCEPTION_INV_PRF_CP)

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
			raise ValueError(EXCEPTION_INV_PRF_CS)

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
			raise ValueError(EXCEPTION_INV_PRF_AV)

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
			raise ValueError(EXCEPTION_INV_PRF_SX)

	@sex.deleter
	def sex(self):
		del self.__sex


class Student(User):
	""" Last, but not least, the Student.
		The main user of this software. Students are allowed to take courses, answer to exercises and lots of fun stuff.
	"""
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
			raise ValueError(EXCEPTION_INV_STU_MT)

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
			raise ValueError(EXCEPTION_INV_STU_BS)

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
			raise ValueError(EXCEPTION_INV_STU_CP)

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
			raise ValueError(EXCEPTION_INV_STU_CO)

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
			raise ValueError(EXCEPTION_INV_STU_AV)

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
			raise ValueError(EXCEPTION_INV_STU_SX)

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
			raise ValueError(EXCEPTION_INV_STU_ML)

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
			raise ValueError(EXCEPTION_INV_STU_GR)

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
			raise ValueError(EXCEPTION_INV_STU_IN)

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
			raise ValueError(EXCEPTION_INV_STU_LN)

	@language.deleter
	def language():
		del __language


class Courses:
	""" The master level of organization of the system.
		A course holds modules, that holds lessons, that holds exercises. They're basically the highest level of abstraction in this system. Usually, one professor will be given an empty course, from wich he'll build the smaller parts of his student's journey.
	"""

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
			raise ValueError(EXCEPTION_INV_CRS_NM)

	@property
	def thisId(self):
		return self.__thisId

	@thisId.setter
	def thisId(self, thisId):
		if type(thisId) is Id:
			self.__thisId = thisId
		else:
			raise ValueError(EXCEPTION_INV_CRS_ID)

	@property
	def students(self):
		return self.__students

	@students.setter
	def students(self, students):
		if type(students) is list and (type(students[0]) is Id or not students):
			self.__students = students
		else:
			raise ValueError(EXCEPTION_INV_CRS_ST)

	@property
	def modules(self):
		return self.__modules		

	@modules.setter
	def modules(self, modules):
		if type(modules) is list and (type(modules[0]) is Id or not modules):
			self.__modules = modules
		else:
			raise ValueError(EXCEPTION_INV_CRS_MD)

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


class Module:
	""" The intermedium.
		Modules holds lessons. They're like "levels" of a game. Get one, unlock another. It is fun, admit.
	"""
	def __init__(self, name, thisId, lessonIdList):
		try:
			self.name = name
			self.thisId = thisId
			self.lessons = lessonIdList
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
			raise ValueError(EXCEPTION_INV_MD_NM)

	@name.deleter
	def name(self):
		del self.__name


	@property
	def thisId(self):
		return self.__thisId

	@name.setter
	def thisId(self, thisId):
		if type(thisId) is Id:
			self.__thisId = thisId
		else:
			raise ValueError(EXCEPTION_INV_MD_ID)

	@name.deleter
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
			raise ValueError(EXCEPTION_INV_MD_LT)

	@lessons.deleter
	def lessons(self):
		del self.__lessons

class Lesson:
	""" One of the building blocks behind everything: lessons.
		They're capable of being about everything you want them do be. Video, audio, slideshow, anything. Just put what you wanna show in the html file and store it as a link. Be happy, then.
	"""

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
			raise ValueError(EXCEPTION_INV_LS_NM)

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
			raise ValueError(EXCEPTION_INV_LS_ID)

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
			raise ValueError(EXCEPTION_INV_LS_LK)

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
			raise ValueError(EXCEPTION_INV_LS_ST)

	@exercises.deleter
	def exercises(self):
		del self.__exercises

class Exercise:
	""" The main learning unit of the system. 
		It is by exercising that humans do learn a new skill. This is a very important class, then. Take care of it.
	"""

	def __init__(self, thisId, link, extType, exFormat, items):
		try:
			self.thisId = thisId
			self.link = link
			self.exType = exType
			self.exFormat = exFormat
			self.items = items
		except VaelueError as exc:
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
			raise ValueError(EXCEPTION_INV_EX_ID)

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
			raise ValueError(EXCEPTION_INV_EX_LK)

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
			raise ValueError(EXCEPTION_INV_EX_ET)

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
			raise ValueError(EXCEPTION_INV_EX_FT)

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
			raise ValueError(EXCEPTION_INV_EX_IT)

	@items.deleter
	def items(self):
		del self.__items
