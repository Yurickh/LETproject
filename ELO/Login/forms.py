#coding: utf-8

from django import forms
from ELO.BaseUnit import Name, Password

""" Form class for the Login Form.
	It receives a username and a password and passes it to the LoginUnit for validation """
class LoginForm(forms.Form):
	username = forms.CharField(max_length = 32, label = "Username")
	password = forms.CharField(widget = forms.PasswordInput, label = "Password")
	
	def clean_username(self):
		try:
			name = Name(self.cleaned_data['username'])
		except ValueError:
			raise forms.ValidationError("Login ou senha inválidos.")
		return name

	def clean_password(self):
		try:
			pw = Password(self.cleaned_data['password'])
		except ValueError:
			raise forms.ValidationError("Login ou senha inválidos.")
		return pw
