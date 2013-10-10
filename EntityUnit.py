#coding: utf-8

from baseUnit import *
from abc import *
from lang.pt_br import *

class User:
	__metaclass__ = ABCMeta

	__instantiable = abstractproperty()

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
	_User__instantiable = True

	def __init__(self, name, password):
		try:
			self.name = name
			self.password = password
		except ValueError as exc:
			del self
			raise exc

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

class Courses:

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
	def delName(self):
		del _name

	@thisId.deleter
	def delthisId(self):
		del _thisId

	@students.deleter
	def delStudents(self):
		del _students

	@modules.deleter
	def delModules(self):
		del _modules


class Module:
	
	def __init__(self, name, thisId, lectureIdList):
		try:
			self.name = name
			self.thisId = thisId
			self.lectures = lectureIdList
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
	def lectures(self):
		return self.__lectures

	@lectures.setter
	def lectures(self, lectures):
		if type(lectures) is list and (type(lectures[0]) is Id or not lectures):
			self.__lectures = lectures
		else:
			raise ValueError(EXCEPTION_INV_MD_LT)