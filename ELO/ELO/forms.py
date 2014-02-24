#coding: utf-8

from django import forms
from ELO.BaseUnit import Name, Password
from lang.pt_br import *

## Classe de formulário para o formulário de Login.
# Recebe um username e um password e passa para o LoginUnit para a validacao."""
class LoginForm(forms.Form):
	username = forms.CharField(max_length = 32)
	password = forms.CharField(widget = forms.PasswordInput)
	
	## Verifica se a formatação do nome está correta.
	# Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_username(self):
		try:
			name = Name(self.cleaned_data['username'])
		except ValueError:
			raise forms.ValidationError(EXCEPTION_INV_LOG)
		return name

	## Verifica se a formatação do password está correta.
	# Caso esteja, retorna o password, caso contrário, lança uma escessão.
	def clean_password(self):
		try:
			pw = Password(self.cleaned_data['password'])
		except ValueError:
			raise forms.ValidationError(EXCEPTION_INV_LOG)
		return pw
