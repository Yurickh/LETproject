#coding: utf-8

## @file ProfileForms
#	Define as classes que gerarão as forms contidas na página de perfil
#	completa do usuário.

from django import forms

class NameForm(forms.Form):
	newname 	= forms.CharField(max_length=32)
	password 	= forms.CharField(widget=forms.PasswordInput)

	def clean_newname(self):
		try:
			name = Name(self.cleaned_data['newname'])
		except ValueError as exc:
			raise forms.ValidationError(exc.message)
		return name

	def clean_password(self):
		try:
			pw = Password(self.cleaned_data['password'])
		except ValueError as exc:
			raise forms.ValidationError(exc.message)
		return pw

class LanguageForm(forms.Form):

	newlang		= forms.ChoiceField(widget=forms.radioSelect, choices = [
											('Português', 'pt_br'),
											('Inglês',    'en_us')
												]

	def clean_newlang(self):
		newlang = self.cleaned_data['newlang']
		if newlang in available_langs:
			return newlang
		else:
			raise forms.ValidationError(DICT["EXCEPTION_INV_LG_F"])