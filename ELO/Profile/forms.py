#coding: utf-8

## @file ProfileForms
#	Define as classes que gerarão as forms contidas na página de perfil
#	completa do usuário.

from django import forms

from ELO.lang.index import DICT
from ELO.BaseUnit import(
	Name,
	Sex,
	PlainText)

class NameForm(forms.Form):
	newname 	= forms.CharField(max_length=32)
	password 	= forms.CharField(widget=forms.PasswordInput)

	def clean_newname(self):
		try:
			name = Name(self.cleaned_data['new_name'])
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
	newlang		= forms.ChoiceField(widget=forms.RadioSelect, choices = [
											(DICT['PORTUGUESE'], 'pt_br'),
											(DICT['ENGLISH'],    'en_us')
												])

	def clean_newlang(self):
		newlang = self.cleaned_data['new_lang']
		if newlang in available_langs:
			return newlang
		else:
			raise forms.ValidationError(DICT["EXCEPTION_INV_LG_F"])

class SexForm(forms.Form):
	newsex		= forms.ChoiceField(widget=forms.RadioSelect, choices = [
											(DICT['SEX_FEMALE'], 'F'),
											(DICT['SEX_MALE'],	 'M')
												])

	def clean_newsex(self):
		try:
			ns = Sex(self.cleaned_data['new_sex'])
		except ValueError as exc:
			raise forms.ValidationError(exc.message)
		return ns

class BiosForm(forms.Form):
	newbios		= forms.TextField(widget=forms.TextArea)

	def clean_newbios(self):
		try:
			nb = PlainText(self.cleaned_data['new_bios'])
		except ValueError as exc:
			raise forms.ValidationError(exc.message)
		return nb