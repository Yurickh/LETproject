#coding: utf-8

from django import forms
from ELO.BaseUnit import Name, Password

##package AdmForms
# Este arquivo define os formulários do módulo de Administração, como os formulários de cadastro de aluno, remoção de aluno, e etc.


## Classe de formulário para o formulário de cadastro de aluno.
# O administrador entra com o nome do aluno, a senha desse aluno para o cadastro do aluno, validanto o cadastro com a senha de administrador.
class AdmRegStuForm(forms.Form):
	studName = forms.charField(max_length = 32, label = "Nome do estudante")
	studPass = forms.CharField(widget = forms.PasswordInput, label = "Senha do estudante") 
	studMatric =
	studCampus =
	studEmail = 
	studSex = 
	admPass = forms.CharField(widget = forms.PasswordInput, label = "Sua senha")

	## Verifica se a formatação do nome de aluno está correta.
	# Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_studName(self):
		try:
			name = Name(self.cleaned_data['studName'])
		except ValueError:
			raise forms.ValidationError("Nome de aluno inválido.")
		return name

	## Verifica se a formatação da senha de aluno está correta.
	# Caso esteja, retorna a senha, caso contrário, lança uma excessão.
	def clean_studPass(self):
		try:
			password = Password(self.cleaned_data['studPass']
		except ValueError:
			raise forms.ValidationError("Senha de aluno inválida.")

	## Verifica se a formatação da senha do administrador está correta.
	# Caso esteja, retorna a senha, caso contrário, lança uma excessão.
	def clean_admPass(self):
		try:
			password = Password(self.cleaned_data['admPass']
		except ValueError:
			raise forms.ValidationError("Senha inválida.")


class AdmDelStuForm: pass

class AdmRegProfForm(forms.Form): pass





class AdmDelProfForm: pass
