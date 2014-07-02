#coding: utf-8

## @file ProfileForms
#	Define as classes que gerarão as forms contidas na página de perfil
#	completa do usuário.

from django import forms

import ELO.locale.index as lang
from ELO.BaseUnit import(
	Name,
	Sex,
	PlainText,
	Password)

## Formulário de edição de nome.
#	Capaz de modificar o nome do usuário no sistema.
#	Vale salientar que é com esse nome que o usuário irá logar.
class NameForm(forms.Form):
	newdata 	= forms.CharField(max_length=32)
	password 	= forms.CharField(widget=forms.PasswordInput)

	def clean_newdata(self):
		try:
			name = Name(self.cleaned_data['newdata'])
		except ValueError as exc:
			raise forms.ValidationError(exc)
		return name

	def clean_password(self):
		try:
			pw = Password(self.cleaned_data['password'])
		except ValueError as exc:
			raise forms.ValidationError(exc)
		return pw

## Formulário de edição de linguagem.
#	Capaz de modificar a lingaguem preferida do usuário para o sistema.
#	É com base nessa linguagem que o sistema irá carregar os diferentes DICTs
#	do site (o dicionário contendo a nomeação de todas as macros).
class LanguageForm(forms.Form):
	newdata		= forms.ChoiceField(widget=forms.RadioSelect, choices = [
											('pt-br', lang.DICT['PORTUGUESE']),
											('en', lang.DICT['ENGLISH'])
												])

	def clean_newdata(self):
		newlang = self.cleaned_data['newdata']
		if newlang in lang.available_langs:
			return newlang
		else:
			if newlang[:newlang.index('-')] in lang.available_langs:
				return newlang
			else:
				raise forms.ValidationError(lang.DICT["EXCEPTION_INV_LG_F"])

## Formulário de edição de sexo.
#	Capaz de modificar o sexo exibido do usuário.
#	Não afeta de forma relevante a navegação ou qualquer outra forma de
#	interação com o aluno/professor.
class SexForm(forms.Form):
	newdata		= forms.ChoiceField(widget=forms.RadioSelect, choices = [
											('F', lang.DICT['SEX_FEMALE']),
											('M', lang.DICT['SEX_MALE'])
												])

	def clean_newdata(self):
		try:
			ns = Sex(self.cleaned_data['newdata'])
		except ValueError as exc:
			raise forms.ValidationError(exc)
		return ns

## Formulário de edição de Bios.
#	Capaz de modificar a biografia exibida do usuário.
#	Não afeta de forma relevante a navegação ou qualquer outra forma de
#	interação com o aluno.
class BiosForm(forms.Form):
	newdata		= forms.CharField(widget=forms.Textarea(attrs={'style':'width:90%;'}))

	def clean_newdata(self):
		try:
			nb = PlainText(self.cleaned_data['newdata'])
		except ValueError as exc:
			raise forms.ValidationError(exc)
		return nb

## Formulário de edição de interesses.
#	Capaz de modificar a lista de interesses do jovem usuário.
#	Talvez venhamos a utilizar isso mais para frente.
class InterestsForm(forms.Form):
	newdata		= forms.CharField(widget=forms.Textarea(attrs={'id':'interests', 'style':'width:90%;'}))

	def clean_newdata(self):
		try:
			nb = PlainText(self.cleaned_data['newdata'])
		except ValueError as exc:
			raise forms.ValidationError(exc)
		return nb