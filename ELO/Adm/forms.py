#coding: utf-8

## @file AdmForms
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

## Classe para o formulário de cadastro de aluno, professor ou administrador.
#	O administrador insere os dados do usuario a ser
#	cadastrado, validando o cadastro com a senha de administrador.
class RegUserForm(forms.Form):
	username = forms.CharField(max_length = 32, label = "Nome:", 
								required= True)
	userMatric = forms.IntegerField(label = "Matricula:",required= True)
	userCampus = forms.IntegerField(label = "Código do Campus:",
									required= True) 
	userSex = forms.ChoiceField(choices=[('M','M'),("F",'F')], 
								widget=forms.RadioSelect(),
								required= True, label = "Sexo")
	userEmail =  forms.EmailField(label = "Email:", required= True)
	userPassword = forms.CharField(widget = forms.PasswordInput(
								attrs={'autocomplete':'off'}), 
								label = "Sua senha",required= True)
	
	## Verifica se a formatação do nome do usuário está correta.
	#	Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_username(self):
		try:
			name = Name(self.cleaned_data["username"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_LOG"])
		return name

	## Verifica se a formatação da matrícula do usuário está correta.
	#	Caso esteja, retorna a matrícula, caso contrário, lança uma excessão.
	def clean_userMatric(self):
		try:
			matric = Matric(self.cleaned_data["userMatric"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_MT"])
		return matric

	## Verifica se a formatação do número de Campus do usuário está correta.
	#	Caso esteja, retorna o número de Campus, caso contrário, 
	#	lança uma excessão.
	def clean_userCampus(self):
		try:
			campus = Campus(self.cleaned_data["userCampus"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_CP"])
		return campus

	## Verifica se a formatação do sexo do usuário está correta.
	#	Caso esteja, retorna o sexo, caso contrário, lança uma excessão.
	def clean_userSex(self):
		try:
			sex = Sex(self.cleaned_data["userSex"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_SX"])
		return sex

	## Verifica se a formatação do email do usuario está correta.
	#	Caso esteja, retorna o e-mail, caso contrário, lança uma excessão.
	def clean_userEmail(self):
		try:
			email = Mail(self.cleaned_data["userEmail"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_ML"])
		return email	
	
	## Verifica se a formatação da senha do usuario está correta.
	#	Caso esteja, retorna a senha, caso contrário, lança uma excessão.
	def clean_userPassword(self):
		try:
			password = Password(self.cleaned_data['userPassword'])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_LOG"])
		return password

class RegAdmForm(forms.Form):
	username = forms.CharField(max_length = 32, label = "Nome:", 
								required= True)
	userEmail =  forms.EmailField(label = "Email:", required= True)
	userPassword = forms.CharField(widget = forms.PasswordInput(
								attrs={'autocomplete':'off'}), 
								label = "Sua senha",required= True)
	
	## Verifica se a formatação do nome do usuário está correta.
	#	Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_username(self):
		try:
			name = Name(self.cleaned_data["username"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_LOG"])
		return name

	## Verifica se a formatação do email do usuario está correta.
	#	Caso esteja, retorna o e-mail, caso contrário, lança uma excessão.
	def clean_userEmail(self):
		try:
			email = Mail(self.cleaned_data["userEmail"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_ML"])
		return email	
	
	## Verifica se a formatação da senha do usuario está correta.
	#	Caso esteja, retorna a senha, caso contrário, lança uma excessão.
	def clean_userPassword(self):
		try:
			password = Password(self.cleaned_data['userPassword'])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_LOG"])
		return password

## Classe para o formulário de pesquisa de aluno, professor, tutor 
# ou administrador.
#	O administrador insere o nome do usuario a ser pesquisado.
class SrcUserForm(forms.Form): 
	username = forms.CharField(max_length = 32, label = "", required=True,
								widget=forms.TextInput(
								attrs={'placeholder':"Name"}))
	
	## Verifica se a formatação do nome do usuário está correta.
	#	Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_username(self):
		try:
			name = Name(self.cleaned_data["username"])
		except ValueError:
			raise forms.ValidationError("Usário inválido.")
		return name
		
## Classe para o formulário de confirmação de senha do administrador.
class ConfAdmForm(forms.Form):
	admPassword = forms.CharField(widget = forms.PasswordInput, 
							label = "Senha do Adm",
							required= True)

	## Verifica se a formatação da senha do administrador está correta.
	#	Caso esteja, retorna a senha, caso contrário, lança uma excessão.
	def clean_admPass(self):
		try:
			password = Password(self.cleaned_data['admPassword'])
		except ValueError:
			raise forms.ValidationError("Senha inválida.")
		return password 

## Classe para o formulário de cadastro de curso.
#	O administrador insere os dados do curso a ser
#	cadastrado, validando o cadastro com a senha de administrador.
class RegCourForm(forms.Form):
	courMatric=forms.IntegerField(label= "Código da Disciplina", 
								required = True)
	courName= forms.CharField(max_length = 32, label ="Nome da Disciplina", 
							required = True)
	courProfessor = forms.CharField( max_length = 32, 
									label = "Nome do Professor da Disciplina", 
									required = True)
      
    ## Verifica se a formatação da matrícula do curso está correta.
	#	Caso esteja, retorna a matrícula, caso contrário, lança uma excessão.
	def clean_courMatric(self):
		try:
			matric = Matric(self.cleaned_data["courMatric"])
		except ValueError:
			raise forms.ValidationError("Código da Disciplina inválido.")
		return matric

	## Verifica se a formatação do nome do curso está correta.
	#	Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_courName(self):
		try:
			name = Name(self.cleaned_data["courName"])
		except ValueError:
			raise forms.ValidationError("Nome de Disciplina Inválido")
		return name

	## Verifica se a formatação do nome do Professor responsável do curso 
	##	está correta.
	#	Caso esteja, retorna o nome do Professor, caso contrário, lança
	#	uma excessão.
	def clean_courProfessor(self):
		try:
			professor = Name(self.cleaned_data["courProfessor"])
		except ValueError:
			raise forms.ValidationError("Nome de Professor Inválido")
		return professor				

## Classe para o formulário de procura de curso.
#	O administrador insere a matrícula do curso a ser pesquisado.
class SrcCourForm(forms.Form):
	courMatric = forms.IntegerField(label = "Código da Disciplina", 
								required =True, widget=forms.TextInput(
									attrs={'placeholder':"Number"}))

	## Verifica se a formatação da matrícula do curso está correta.
	#	Caso esteja, retorna a matrícula, caso contrário, lança uma excessão.
	def clean_courMatric(self):
		try:
			matric = Matric(self.cleaned_data["courMatric"])
		except ValueError:
			raise forms.ValidationError("Código Inválido")
		return matric

class EditUserForm(forms.Form):
	username = forms.CharField(label = "Nome:", widget = forms.TextInput(attrs={'readonly':'readonly'}))
	userMatric = forms.IntegerField(label = "Matricula:",required= True)
	userCampus = forms.IntegerField(label = "Código do Campus:",
									required= True) 
	userSex = forms.ChoiceField(choices=[('M','M'),("F",'F')], 
								widget=forms.RadioSelect(),
								required= True, label = "Sexo")
	userEmail =  forms.EmailField(label = "Email:", required= True)
	
	## Verifica se a formatação do nome do usuário está correta.
	#	Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_username(self):
		try:
			name = Name(self.cleaned_data["username"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_LOG"])
		return name

	## Verifica se a formatação da matrícula do usuário está correta.
	#	Caso esteja, retorna a matrícula, caso contrário, lança uma excessão.
	def clean_userMatric(self):
		try:
			matric = Matric(self.cleaned_data["userMatric"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_MT"])
		return matric

	## Verifica se a formatação do número de Campus do usuário está correta.
	#	Caso esteja, retorna o número de Campus, caso contrário, 
	#	lança uma excessão.
	def clean_userCampus(self):
		try:
			campus = Campus(self.cleaned_data["userCampus"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_CP"])
		return campus

	## Verifica se a formatação do sexo do usuário está correta.
	#	Caso esteja, retorna o sexo, caso contrário, lança uma excessão.
	def clean_userSex(self):
		try:
			sex = Sex(self.cleaned_data["userSex"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_SX"])
		return sex

	## Verifica se a formatação do email do usuario está correta.
	#	Caso esteja, retorna o e-mail, caso contrário, lança uma excessão.
	def clean_userEmail(self):
		try:
			email = Mail(self.cleaned_data["userEmail"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_ML"])
		return email	

class EditCourForm(forms.Form):
	courMatric=forms.IntegerField(label= "Código da Disciplina", 
								widget = forms.TextInput(attrs={'readonly':'readonly'}))
	courName= forms.CharField(max_length = 32, label ="Nome da Disciplina", 
							required = True)
	courProfessor = forms.CharField( max_length = 32, 
									label = "Nome do Professor da Disciplina", 
									required = True)
      
    ## Verifica se a formatação da matrícula do curso está correta.
	#	Caso esteja, retorna a matrícula, caso contrário, lança uma excessão.
	def clean_courMatric(self):
		try:
			matric = Matric(self.cleaned_data["courMatric"])
		except ValueError:
			raise forms.ValidationError("Código da Disciplina inválido.")
		return matric

	## Verifica se a formatação do nome do curso está correta.
	#	Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_courName(self):
		try:
			name = Name(self.cleaned_data["courName"])
		except ValueError:
			raise forms.ValidationError("Nome de Disciplina Inválido")
		return name

	## Verifica se a formatação do nome do Professor responsável do curso 
	##	está correta.
	#	Caso esteja, retorna o nome do Professor, caso contrário, lança
	#	uma excessão.
	def clean_courProfessor(self):
		try:
			professor = Name(self.cleaned_data["courProfessor"])
		except ValueError:
			raise forms.ValidationError("Nome de Professor Inválido")
		return professor

class EditAdmForm(forms.Form):
	username = forms.CharField(label = "Nome:", 
								widget = forms.TextInput(attrs={'readonly':'readonly'}))
	userEmail =  forms.EmailField(label = "Email:", required= True)
	
	## Verifica se a formatação do nome do usuário está correta.
	#	Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_username(self):
		try:
			name = Name(self.cleaned_data["username"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_LOG"])
		return name

	## Verifica se a formatação do email do usuario está correta.
	#	Caso esteja, retorna o e-mail, caso contrário, lança uma excessão.
	def clean_userEmail(self):
		try:
			email = Mail(self.cleaned_data["userEmail"])
		except ValueError:
			raise forms.ValidationError(lang.DICT["EXCEPTION_INV_STU_ML"])
		return email	


