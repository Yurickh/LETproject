#coding utf-8

from abc import *
from django.shortcuts import render
from ELO.forms import LoginForm
from django.template import Template, Context
from django import forms
from ELO.BaseUnit import Name, Password

from django.http import HttpResponseRedirect

class IfUiLogin:
	__metaclass__ = ABCMeta

	@abstractmethod
	def run(self, request): pass

	@abstractmethod
	def setBusLogin(self, busLogin): pass

class IfBusLogin: 
	__metaclas__ = ABCMeta

	@abstractmethod
	def validate(self, username, password): pass

	@abstractmethod
	def setPers(self, pers): pass
	
class UiLogin(IfUiLogin):

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
		if isinstance(value, IfBusLogin):
			self.__bus = value
		else:
			raise TypeError("Expected IfBusLogin instance at UiLogin.__bus. Received " + str(type(value)) + " instead.")

	@bus.deleter
	def bus(self):
		del self.__bus

	def run(self, request):
		if request.method == "POST":
			login_form = LoginForm(request.POST)
			try: 
				if login_form.is_valid():
					self.__bus.validate(login_form.cleaned_data['username'], login_form.cleaned_data['password'])
				else:
					raise ValueError()
			except ValueError as exc:
				return render(request, "loginpage.html", {'form': login_form, 'error': exc})
			else:
				request.session['USER'] = login_form.cleaned_data['username']
				return HttpResponseRedirect('/profile')
		else:
			if 'USER' in request.session.keys():
				return render(request, "profile.html", {'user': request.session['USER']})
			login_form = LoginForm()
			return render(request, "loginpage.html", {'form': login_form})

class BusLogin(IfBusLogin):

	__pers = None

	def validate(self, username, password):
		try:
			if username != Name(u"Adm") or password != Password(u"123456"):
				raise ValueError("Login ou senha incorretos.")
		except ValueError as exc:
			raise exc

	def setPers(self, pers):
		self.__pers = pers
