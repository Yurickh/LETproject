#coding utf-8

from abc import *
from django.shortcuts import render
from ELO.forms import LoginForm

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
	__bus = None

	def run(self, request):
		if request.method == "POST":
			login_form = LoginForm(request.POST)
			errors = []
			if login_form.is_valid():
				BusLogin.validate(cleaned_data['username'], cleaned_data['password'])
				return render(request, "loginsuccess.html", {'user': BusLogin})
			else:
				errors.append("Dados incorretos")
				return render(request, "loginpage.html", {'errors': errors, 'form': login_form})
		else:
			login_form = LoginForm()
			return render(request, "loginpage.html", {'form': login_form})

	def setBusLogin(self, busLogin):
		self.__bus = busLogin

class BusLogin(IfBusLogin):

	__pers = None

	def validate(self, username, password):
		try: 
			self.username != "adm"
			self.password != "123"
		except ValueError as exc:
			raise exc

	def setPers(self, pers):
		self.__pers = pers
