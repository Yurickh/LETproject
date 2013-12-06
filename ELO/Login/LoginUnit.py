#coding utf-8

""" This file is responsible for storing all the layers that deal with the Login module.
	The methods here are created and called by the Factory (MainUnit.py) when necessary.
	They're responsible for creation, management and deletion of the session object and the validation and login of users.
"""

from abc import *
from django.shortcuts import render
from ELO.forms import LoginForm
from django.template import Template, Context
from django import forms
from django.forms import ValidationError
from ELO.BaseUnit import Name, Password

from django.http import HttpResponseRedirect

""" Interface for the User Interface layer of the Login module.
	It is responsible for loading the right template and process the data inputted in the login form.
"""
class IfUiLogin:
	__metaclass__ = ABCMeta

	""" Enforces the existance of the underlaying layer """
	def __init__(self, bus):
		try:
			self.bus = bus
		except TypeError as exc:
			del self
			raise exc

	""" Business layer associated to the UI layer. They're linked in the MainUnit module """
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

	""" The main method of any UI class, the run() method allows the Factory to give control over the program to the given module.
	"""
	@abstractmethod
	def run(self, request): pass

""" Interface for the Business layer of the Login module.
	It is responsible for the validation of the data submitted throught the login form.
"""
class IfBusLogin: 
	__metaclas__ = ABCMeta

	""" The validation method returns nothing, but raises an exception if the validation isn't successful. """
	@abstractmethod
	def validate(self, username, password): pass

	""" This method shall be deleted """
	@abstractmethod
	def setPers(self, pers): pass

""" User Interface layer for the Login module """
class UiLogin(IfUiLogin):

	def run(self, request):
		if request.method == "POST":
			login_form = LoginForm(request.POST)
			try: 
				if login_form.is_valid():
					self.bus.validate(login_form.cleaned_data['username'], login_form.cleaned_data['password'])
				else:
					raise ValidationError("Login ou senha incorretos")
			except ValidationError as exc:
				return render(request, "loginpage.html", {'form': login_form, 'error': exc})
			else:
				request.session['USER'] = login_form.cleaned_data['username']
				return HttpResponseRedirect('/profile')
		else:
			login_form = LoginForm()
			return render(request, "loginpage.html", {'form': login_form})

""" Business layer for the Login module """
class BusLogin(IfBusLogin):

	__pers = None

	def validate(self, username, password):
		if username != Name(u"Adm") or password != Password(u"123456"):
			raise ValidationError("Login ou senha incorretos.")

	def setPers(self, pers):
		self.__pers = pers
