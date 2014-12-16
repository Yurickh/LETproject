#coding: utf-8

from abc import*

import ELO.locale.index as lang

from ELO.models import Courses, Module, Lesson, Student

from Course.forms import LessonForm

from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.forms import ValidationError

LESSONS_URL = 'Course/lessons/'
GENERAL_URL = 'Course/general/'

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
	def run(self, request, courseid=None): pass


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


	## Método que recupera uma lista dos módulos ou lições.
	#
	#	@arg user		Objeto usuário, como no contido no cookie user.
	#
	#	@arg accesstype	String contendo "MODULE" ou "LESSON"
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

	def run(self, request, courseid=None):
		
		user = request.session['user']

		if request.method == "GET":
			if courseid:
				if courseid in map(lambda x: x["id"], user["courses"]):
					course = self.bus.getCourse(user, courseid)
					return render(request, GENERAL_URL + "frame.html", 
						{'course':course})
				else:
					raise PermissionDenied(lang.DICT["EXCEPTION_403_STD"])
		elif request.method == "POST":
			lesson_form = LessonForm(request.POST)
			try:
				if lesson_form.is_valid():
					lessonid = lesson_form.cleaned_data['lesson_id']
					slidenumber = lesson_form.cleaned_data['slide_number']

					lesson = self.bus.getLesson(user, lessonid.value)

					if(slidenumber.value >= lesson['slides']):
						raise PermissionDenied(lang.DICT["EXCEPTION_403_STD"])

					url = LESSONS_URL + lesson['url']
					url = url + "/" + str(slidenumber.value) + ".html"
					return render(request, url)
				else:
					raise ValueError(lang.DICT['EXCEPTION_INV_LES'])
			except ValueError as exc:
				return render(request, GENERAL_URL + "assync_std.html",
						{'error': exc})
				

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
				lessonlist = lessonlist + [{'id': lessonid,
											'name':lessoname[0],
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

	def getLesson(self, user, lessonid):
		lessondata = self.pers.fetch(lessonid, Lesson)

		lesson = {}
		lesson['url'] = lessondata['LINK'][0]
		lesson['name'] = lessondata['NAME'][0]
		lesson['slides'] = lessondata['SLIDES'][0]

		return lesson


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
