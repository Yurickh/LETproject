from django import forms
from ELO.BaseUnit import Name, Password

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 32, label = "Username")
	password = forms.CharField(widget = forms.PasswordInput, label = "Password")
	
	def clean_username(self):
		try:
			name = Name(self.cleaned_data['username'])
		except ValueError as exc:
			raise forms.ValidationError(exc)
		return name

	def clean_password(self):
		try:
			pw = Password(self.cleaned_data['password'])
		except ValueError as exc:
			raise forms.ValidationError(exc)
		return pw
