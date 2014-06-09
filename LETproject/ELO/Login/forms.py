#coding: utf-8

from django import forms
from ELO.BaseUnit import Name, Password

## @package LoginForms
# Este arquivo define os formulários do módulo de Login no sistema.


## Classe de formulário para o fomulário de Login.
# Recebe o username e o password e passa para a LoginUnit para ser validado.
class LoginForm(forms.Form):
	username = forms.CharField(max_length = 32, label = "Username")
	password = forms.CharField(widget = forms.PasswordInput, label = "Password")
	
	## Verifica se a formatação do nome está correta.
	# Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_username(self):
		try:
			name = Name(self.cleaned_data['username'])
		except ValueError:
			raise forms.ValidationError("Login ou senha inválidos.")
		return name

	## Verifica se a formatação do password está correta.
	# Caso esteja, retorna o password, caso contrário, lança uma excessão.
	def clean_password(self):
		try:
			pw = Password(self.cleaned_data['password'])
		except ValueError:
			raise forms.ValidationError("Login ou senha inválidos.")
		return pw
