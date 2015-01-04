#coding: utf-8

from django import forms
from ELO.BaseUnit import Id

import ELO.locale.index as lang

class LessonForm(forms.Form):
    lesson_id = forms.IntegerField(required=True)
    slide_number = forms.IntegerField(required=True)

    def clean_lesson_id(self):
        return Id(self.cleaned_data['lesson_id'])

    def clean_slide_number(self):
        return Id(self.cleaned_data['slide_number'])

class MultipleChoiceExercise(forms.Form):
    options = forms.ChoiceField(widget   = forms.RadioSelect, 
                                required = True)

    def clean_options(self):
        return dict(self.cleaned_data['options'])

class FillTheBlankExercise(forms.Form):
    blank = forms.CharField(required = True)

    def clean_blank(self):
        return PlainText(self.cleaned_data['blank']).value

class UnscrambleExercise(forms.Form):
    bloat = forms.CharField(required = True)

    def clean_bloat(self):
        return self.cleaned_data['bloat'].split()

class CrossWordExercise(forms.Form):
    bloat = forms.CharField(required = True)

    def clean_bloat(self):
        wordList = self.cleaned_data['bloat'].split('_')
        retList = []

        for word in wordList:
            x,y,d,w = word.split()
            retList.append(" ".join([x,y,d,w]))

        return retList