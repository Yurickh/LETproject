from django import forms
from ELO.BaseUnit import Name, Password

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 32, label = "Username")
	password = forms.CharField(widget = forms.PasswordInput, label = "Password")
	
	def clean_username(self):
		return Name(self.cleaned_data['username'])

	def clean_password(self):
		return Password(self.cleaned_data['password'])

