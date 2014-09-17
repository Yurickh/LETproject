#coding: utf-8

## @file ProfileForms
#	Define as classes que gerarão as forms contidas na página de 
#	administração, como os formulários de cadastro, deleção e edição
#	de alunos, professores e cursos.

from django import forms

import ELO.locale.index as lang
from ELO.BaseUnit import(
	Name,
	Sex,
	PlainText,
	Password,
	Link,
	Matric,
	Campus,
	Mail,
	Language)

## Classe de forms para o formulário de cadastro de aluno.
#	O administrador insere os dados do aluno a ser
#	cadastrado, validando o cadastro com a senha de administrador.
class AdmRegStu_ProfForm(forms.Form):
	userName = forms.CharField(max_length = 32, label = "Nome:", required= "True")
	userMatric = forms.IntegerField(label = "Matricula:",required= "True")
	userCampus = forms.IntegerField(label = "Código do Campus:",required= "True") 
	userSex = forms.ChoiceField(choices=[('M','M'),("F",'F')], widget=forms.RadioSelect(),required= "True", label = "Sexo")
	userEmail =  forms.EmailField(label = "Email:", required= "True")
	userPass = forms.CharField(widget = forms.PasswordInput(attrs={'autocomplete':'off'}), label = "Sua senha",required= "True")
	
	## Verifica se a formatação do nome de aluno está correta.
	#	Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_userName(self):
		try:
			name = Name(self.cleaned_data['userName'])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_LOG"])
		return name

	def clean_userMatric(self):
		try:
			matric = Matric(self.cleaned_data["userMatric"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_MT"])
		return matric

	def clean_userCampus(self):
		try:
			campus = Campus(self.cleaned_data["userCampus"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_CP"])
		return campus

	def clean_userSex(self):
		try:
			sex = Sex(self.cleaned_data["userSex"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_SX"])
		return sex

	def clean_userEmail(self):
		try:
			email = Email(self.cleaned_data["userEmail"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_ML"])
		return email	
	
	
	## Verifica se a formatação da senha de aluno está correta.
	#	Caso esteja, retorna a senha, caso contrário, lança uma excessão.
	def clean_userPass(self):
		try:
			password = Password(self.cleaned_data['userPass'])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_LOG"])
		return password


class AdmDelStu_ProfForm(forms.Form): 
	userName = forms.CharField(max_length = 32, label = "Nome:", required= "True")
	
	def clean_userMatric(self):
		try:
			matric = Matric(self.cleaned_data["userMatric"])
		except ValueError:
			raise forms.ValidationError("Usário inválido.")
		return matric
		
class confAdm(forms.Form):
	admPass = forms.CharField(widget = forms.PasswordInput, label = "Senha do Adm",required= "True")

	## Verifica se a formatação da senha do administrador está correta.
	#	Caso esteja, retorna a senha, caso contrário, lança uma excessão.
	def clean_admPass(self):
		try:
			password = Password(self.cleaned_data['admPass'])
		except ValueError:
			raise forms.ValidationError("Senha inválida.")
		return password 

class AdmRegCourForm(forms.Form):
	courMatric=forms.IntegerField(label= "Código da Disciplina", required = "True")
	courName= forms.CharField(max_length = 32, label ="Nome da Disciplina", required = "True")
	courProfessor = forms.CharField( max_length = 32, label = "Nome do Professor da Disciplina", required = "True")
       
	def clean_courMatric(self):
		try:
			matric = Matric(self.cleaned_data["courMatric"])
		except ValueError:
			raise forms.ValidationError("Código da Disciplina inválido.")
		return matric

	def clean_courName(self):
		try:
			name = Name(self.cleaned_data["courName"])
		except ValueError:
			raise forms.ValidationError("Nome de Disciplina Inválido")
		return professor

	def clean_courProfessor(self):
		try:
			professor = Name(self.cleaned_data["courProfessor"])
		except ValueError:
			raise forms.ValidationError("Nome de Professor Inválido")
		return professor			


class AdmSrcCourForm(forms.Form):
	courMatric = forms.IntegerField(label = "Código da Disciplina", required ="True")

	def clean_courMatric(self):
		try:
			courMatric = Matric(self.cleaned_data["courMatric"])
		except ValueError:
			raise forms.ValidationError("Código Inválido")
		return courMatric

class AdmDelCourForm(forms.Form): 
	courMatric = forms.IntegerField(label = "Código da Disciplina", required ="True")

	def clean_courMatric(self):
		try:
			courMatric = Matric(self.cleaned_data["courMatric"])
		except ValueError:
			raise forms.ValidationError("Código Inválido")
		return courMatric#.
