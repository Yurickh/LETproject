#coding: utf-8

## @file LoginForms
# Este arquivo define os formulários do módulo de Login no sistema.

from django import forms
from ELO.BaseUnit import Name, Password

from ELO.lang.index import lang


## Classe de formulário para o fomulário de Login.
# Recebe o username e o password e passa para a LoginUnit para ser validado.
class LoginForm(forms.Form):
	username = forms.CharField(max_length = 32)
	password = forms.CharField(widget = forms.PasswordInput)

	
	## Verifica se a formatação do nome está correta.
	# Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_username(self):
		try:
			name = Name(self.cleaned_data['username'])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_LOG"])
		return name

	## Verifica se a formatação do password está correta.
	# Caso esteja, retorna o password, caso contrário, lança uma excessão.
	def clean_password(self):
		try:
			pw = Password(self.cleaned_data['password'])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_LOG"])
		return pw
