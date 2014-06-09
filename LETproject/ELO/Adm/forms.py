#coding: utf-8

from django import forms
from ELO.BaseUnit import Name, Password

##package AdmForms
# Este arquivo define os formulários do módulo de Administração, como os formulários de cadastro de aluno, remoção de aluno, e etc.


## Classe de formulário para o formulário de cadastro de aluno.
# O administrador entra com o nome do aluno, a senha desse aluno para o cadastro do aluno, validanto o cadastro com a senha de administrador.
class AdmRegStuForm(forms.Form):
	studName = forms.charField(max_length = 32, label = "Nome do estudante"required= "True")
	studPass = forms.CharField(widget = forms.PasswordInput, label = "Senha do estudante",required= "True") 
	studMatric = form.IntergerField(label = "Matricula do estudante",required= "True")
	studCampus = form.IntergerField(label = "Cédigo do Campus",required= "True")
	studEmail =  form.EmailField(label = "Email do estudante", required= "True") 
	studSex = form.ChoiceField(choices=[('M','M'),("F",'F')], widget=forms.RadioSelect(),required= "True", label = "Sexo")
	admPass = forms.CharField(widget = forms.PasswordInput, label = "Sua senha",required= "True")

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
		return password

	def clean_studMatric(self):
		try:
			matric = Matric(self.cleaned_data["studMatric"]
		except ValueError:
			raise forms.ValidationError("Matricula inválida.")
		return matric

	def clean_studSex(self):
		try:
			sex = Sex(self.cleaned_data["studSex"]
		except ValueError:
			raise forms.ValidationError("Sexo inválido.")
		return sex
	
	def clean_studCampus(self):
		try:
			campus = Campus(self.cleaned_data["studCampus"]
		except ValueError:
			raise forms.ValidationError("Código de Campus inválido.")
		return campus

	def clean_studEmail(self):
		try:
			email = Email(self.cleaned_data["studEmail"]
		except ValueError:
			raise forms.ValidationError("Email inválido.")
		return email	 
## Verifica se a formatação da senha do administrador está correta.
	# Caso esteja, retorna a senha, caso contrário, lança uma excessão.
	def clean_admPass(self):
		try:
			password = Password(self.cleaned_data['admPass']
		except ValueError:
			raise forms.ValidationError("Senha inválida.")
		return password 

class AdmDelStuForm(forms.Form): 
	studMatric = form.IntergerField(label = "Matricula do estudante",required= "True")
	admPass = forms.CharField(widget = forms.PasswordInput, label = "Sua senha",required= "True")
	def clean_studMatric(self):
		try:
			matric = Matric(self.cleaned_data["studMatric"]
		except ValueError:
			raise forms.ValidationError("Matricula inválida.")
		return matric
	
	def clean_admPass(self):
		try:
			password = Password(self.cleaned_data["admPassword"]
		except ValueError:
			raise forms.ValidationError("Senha inválida.")
		return password

class AdmRegProfForm(forms.Form): 
	profName = forms.charField(max_length = 32, label = "Nome do Professor"required= "True")
	profPass = forms.CharField(widget = forms.PasswordInput, label = "Senha do Professor",required= "True") 
	profMatric = form.IntergerField(label = "Matricula do Professor",required= "True")
	profCampus = form.IntergerField(label = "Cédigo do Campus",required= "True")
	profEmail =  form.EmailField(label = "Email do Professor", required= "True") 
	profSex = form.ChoiceField(choices=[('M','M'),("F",'F')], widget=forms.RadioSelect(),required= "True", label = "Sexo")
	admPass = forms.CharField(widget = forms.PasswordInput, label = "Sua senha",required= "True")

	## Verifica se a formatação do nome de aluno está correta.
	# Caso esteja, retorna o nome, caso contrário, lança uma excessão.
	def clean_profName(self):
		try:
			name = Name(self.cleaned_data['profName'])
		except ValueError:
			raise forms.ValidationError("Nome de Professor inválido.")
		return name
	
	## Verifica se a formatação da senha de aluno está correta.
	# Caso esteja, retorna a senha, caso contrário, lança uma excessão.
	def clean_profPass(self):
		try:
			password = Password(self.cleaned_data['profPass']
		except ValueError:
			raise forms.ValidationError("Senha de Professor inválida.")
		return password

	def clean_profMatric(self):
		try:
			matric = Matric(self.cleaned_data["profMatric"]
		except ValueError:
			raise forms.ValidationError("Matricula inválida.")
		return matric

	def clean_profSex(self):
		try:
			sex = Sex(self.cleaned_data["profSex"]
		except ValueError:
			raise forms.ValidationError("Sexo inválido.")
		return sex
	
	def clean_profCampus(self):
		try:
			campus = Campus(self.cleaned_data["profCampus"]
		except ValueError:
			raise forms.ValidationError("Código de Campus inválido.")
		return campus

	def clean_profEmail(self):
		try:
			email = Email(self.cleaned_data["profEmail"]
		except ValueError:
			raise forms.ValidationError("Email inválido.")
		return email	 
	## Verifica se a formatação da senha do administrador está correta.
	# Caso esteja, retorna a senha, caso contrário, lança uma excessão.
	def clean_admPass(self):
		try:
			password = Password(self.cleaned_data['admPass']
		except ValueError:
			raise forms.ValidationError("Senha inválida.")
		return password


class AdmDelProfForm(forms.Form): 
	profMatric = form.IntergerField(label = "Matricula do Professor",required= "True")
	admPass = forms.CharField(widget = forms.PasswordInput, label = "Sua senha",required= "True")
	def clean_profMatric(self):
		try:
			matric = Matric(self.cleaned_data["studMatric"]
		except ValueError:
			raise forms.ValidationError("Matricula inválida.")
		return matric
	
	def clean_admPass(self):
		try:
			password = Password(self.cleaned_data["admPassword"]
		except ValueError:
			raise forms.ValidationError("Senha inválida.")
		return password

class AdmRegCourForm(forms.Form):
	courMatric=form.IntergerField(lebel= "Código da Disciplina", required = "True")
	courName= form.CharField(max_length = 32, label ="Nome da Disciplina", required = "True")
	courProfessor = form.CharField( max_length = 32, label = "Nome do Professor da Disciplina", required = "True")
        admPass = forms.CharField(widget =forms.PasswordInput, label = "Sua senha", required = "True")
	
	def clean_courMatric(self):
		try:
			matric = Matric(self.cleaned_data["courMatric"]
		except ValueError:
			raise forms.ValidationError("Código da Disciplina inválido.")
		return matric

	def clean_courName(self):
		try:
			name = Name(self.cleaned_data["courName"]
		except ValueError:
			raise forms.ValidationError("Nome de Disciplina Inválido")
		return professor

	def clean_courProfessor(self):
		try:
			professor = Name(self.cleaned_data["courProfessor"]
		except ValueError:
			raise forms.ValidationError("Nome de Professor Inválido")
		return professor			
	
	def clean_admPass(self):
		try:
			password = Password(self.cleaned_data["admPassword"]
		except ValueError:
			raise forms.ValidationError("Senha inválida.")
		return password 

class AdmDelCourForm(forms.form): pass

class AdmSrcStuForm(forms.form):  
	stuMatric= form.IntergerField(label = "Matricula do Estudante", required = "True")
	
	def clean_studMatric(self):
		try:
			matric = Matric(self.cleaned_data["studMatric"]
		except ValueError:
			raise forms.ValidationError("Matricula inválida.")
		return matric
		
class AdmSrcProfForm(forms.form):
	profMatric = forms.IntergerField(label = "matricula do Professor", required = 'True')
	def clean_profMatric(self):
		try:
			matric = Matric(self.cleaned_data["profMatric"]
		except ValueError:
			raise forms.ValidationError("Matricula inválida.")
		return matric
			

#.
