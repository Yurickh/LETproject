#coding: utf-8

from baseUnit import *
from abc import *

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
	def name(self, name):
		if isinstance(name, Name):
			self._name = name
		else:
			raise ValueError(EXCEPTION_INV_USR_NM)

	@name.setter
	def password(self, password):
		if isinstance(password, Password):
			self._password = password
		else:
			raise ValueError(EXCEPTION_INV_USR_PW)

	def delName(self):
		del self._name

	def delPassword(self):
		del self._password


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
			raise ValueError(EXCEPTION_INV_STU_MT)
	def delMatric(self):
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
	def delBios(self):
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
	def delCampus(self):
		del __campus

	@property
	def courses(self):
		return self.__courses
	@courses.setter
	def courses(self, courses):
		if type(courses[0]) is Id or not courses) and type(courses) is list :
			self.__courses = courses
		else:
			raise ValueError(EXCEPTION_INV_STU_CO)
	def delCourses(self):
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
	def delAvatar(self):
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
	def delSex(self):
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
	def delEmail(self):
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
	def delGrades(self):
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
	def delInterests(self):
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
	def delLanguage():
		del __language


