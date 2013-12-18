#coding: utf-8

""" This file is responsible for storing all the layers that deal with the Login module.
	The methods here are created and called by the Factory (MainUnit.py) when necessary.
	They're responsible for creation, management and deletion of the session object and the validation and login of users.
"""

from abc import *

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import Template, Context
from django import forms

from Login.models import Student
from ELO.BaseUnit import Name, Password
from Login.forms import LoginForm
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

	@property
	def pers(self):
		return self.__pers

	@pers.setter
	def pers(self, pers):
		if isinstance(value, IfPersLogin):
			self.__pers = pers
		else:
			raise TypeError("Expected IfPersLogin instance at BusLogin.__pers. Received " + str(type(value)) + "instead.")

	@pers.deleter
	def pers(self):
		del self.__pers

	""" Enforces the existance of the underlaying layer """
	def __init__(self, value):
		try:
			self.pers = value
		except TypeError as exc:
			del self
			raise exc

class IfPersLogin:

	__metaclass__ = ABCMeta

	@abstractmethod
	def select(self, username): pass

""" User Interface layer for the Login module """
class UiLogin(IfUiLogin):

	def run(self, request):
		if request.method == "POST":
			login_form = LoginForm(request.POST)
			try: 
				if login_form.is_valid():
					self.bus.validate(login_form.cleaned_data['username'], login_form.cleaned_data['password'])
				else:
					raise ValueError("Login ou senha incorretos.")
			except ValueError as exc:
				return render(request, "Login/form.html", {'form': login_form, 'error': exc})
			else:
				request.session['user'] = login_form.cleaned_data['username']
				return HttpResponseRedirect('/profile')
		else:
			login_form = LoginForm()
			return render(request, "Login/form.html", {'form': login_form})

""" Business layer for the Login module """
class BusLogin(IfBusLogin):
	def validate(self, username, password):
		upass = self.pers.select(username.value)
		if not upass or upass['password'] != password.value:
			raise ValueError('Login ou senha incorretos.')

class PersLogin(IfPersLogin):

	def select(self, username=None):
		if not username: return False

		try:
			uid = Student.objects.get(value=username, field='NAME').identity
			upass = Student.objects.get(identity=uid, field='PASSWORD').value
			return {'name': username, 'password': upass}
		except Student.DoesNotExist:
			return False
		
