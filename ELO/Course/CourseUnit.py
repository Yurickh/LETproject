#coding: utf-8

from abc import*

import ELO.locale.index as lang

from ELO.models import Courses, Module, Lesson, Student

from django.shortcuts import render
from django.core.exceptions import PermissionDenied

class IfUiCourse:
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
		if isinstance(value, IfBusCourse):
			self.__bus = value
		else:
			raise TypeError("Expected IfBusCourse instance at UiCourse.__bus. Received " + str(type(value)) + " instead.")

	@bus.deleter
	def bus(self):
		del self.__bus

	@abstractmethod
	def run(self, request, courseid): pass


class IfBusCourse:
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
		if isinstance(value, IfPersCourse):
			self.__pers = value
		else:
			raise TypeError("Expected IfPersCourse instance at BusCourse.__pers. Received " + str(type(value)) + "instead.")

	@pers.deleter
	def pers(self):
		del self.__pers

	@abstractmethod
	def getCompleted(self, user, accesstype): pass

	@abstractmethod
	def getCourse(self, user, courseid): pass

class IfPersCourse:

	@abstractmethod
	def getid(self, field, value, db): pass

	@abstractmethod
	def fetch(self, id, db): pass


class UiCourse(IfUiCourse):

	def run(self, request, courseid):
		
		user = request.session['user']

		if request.method == "GET":
			if courseid in map(lambda x: x["id"], user["courses"]):
				course = self.bus.getCourse(user, courseid)
				return render(request, "Course/general/frame.html", 
					{'course':course})
			else:
				raise PermissionDenied(lang.DICT["EXCEPTION_403_STD"])
		

class BusCourse(IfBusCourse):

	def getCompleted(self, user, accesstype):
		userid = self.pers.getid('NAME', user['name'], Student)
		userdata = self.pers.fetch(userid, Student)

		return userdata.get(accesstype + '_COMPLETED', [])

	def getCourse(self, user, courseid):
		compmlist = self.getCompleted(user, 'MODULE')
		compllist = self.getCompleted(user, 'LESSON')
		coursedata = self.pers.fetch(courseid, Courses)
		modulelist = []
		
		for moduleid in coursedata['MODULE']:
			sfm = self.pers.fetch(moduleid, Module)
			modulename = sfm['NAME'][0]

			lessonlist = []

			for lessonid in sfm['LESSON']:
				lessoname = self.pers.fetch(lessonid, Lesson)['NAME']
				lessoncomplete = True if lessonid in compllist else False
				print lessoncomplete
				lessonlist = lessonlist + [{'name':lessoname[0],
										   'complete':lessoncomplete }]

			modulelist = modulelist + [{'id': 		moduleid,
										'name': 	modulename,
										'lessons':	lessonlist,
										'complete':True \
											if moduleid in compmlist \
											else False
									  }]
		
		coursedata['MODULE'] = sorted(modulelist, key=lambda x: x['id'])

		return coursedata


class PersCourse(IfPersCourse):

	def getid(self, field, value, db):
		model_data = db.objects.get(field=field, value=value)
		return model_data.identity

	def fetch(self, id, db):
		model_data = db.objects.filter(identity=id)
		format_data = {}

		## @for
		#	Cria um dicionário de listas, no fomato:
		#
		#	CAMPO_NO_BANCO_DE_DADOS => [ VALOR_1, VALOR_2 ... VALOR_N ]
		for i in model_data.values():
			format_data[i['field']]=format_data.get(i['field'],[])+[i['value']]

		return format_data
