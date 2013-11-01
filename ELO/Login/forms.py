from django import forms

from ELO.BaseUnit import Name, Password

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		return Name(self.cleaned_data['username'])

	def clean_password(self):
		return Password(self.cleaned_data['password'])