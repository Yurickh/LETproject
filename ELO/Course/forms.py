#coding: utf-8

from django import forms
from ELO.BaseUnit import Id

import ELO.locale.index as lang

class LessonForm(forms.Form):
	id = forms.IntegerField(required=True)

	def clean_id(self):
		try:
			id = Id(self.cleaned_data['id'])
		except ValueError as exc:
			raise forms.ValidationError(lang.DICT['EXCEPTION_INV_LES'])