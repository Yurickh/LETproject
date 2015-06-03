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
    exercise_id = forms.IntegerField(required=True, widget=forms.HiddenInput)
    options = forms.ChoiceField(widget   = forms.RadioSelect, 
                                required = True,
                                label = "")

    def clean_options(self):
        return dict(self.cleaned_data['options'])

class FillTheBlankExercise(forms.Form):
    exercise_id = forms.IntegerField(required=True, widget=forms.HiddenInput)
    blank = forms.CharField(required = True, label="")

    def clean_blank(self):
        return PlainText(self.cleaned_data['blank']).value

class UnscrambleExercise(forms.Form):
    exercise_id = forms.IntegerField(required=True, widget=forms.HiddenInput)
    bloat = forms.CharField(required = True, label="")

    def clean_bloat(self):
        return self.cleaned_data['bloat'].split()

class CrossWordExercise(forms.Form):
    exercise_id = forms.IntegerField(required=True, widget=forms.HiddenInput)
    bloat = forms.CharField(required = True, label="")

    def clean_bloat(self):
        wordList = self.cleaned_data['bloat'].split('_')
        retList = []

        for word in wordList:
            x,y,d,w = word.split()
            retList.append(" ".join([x,y,d,w]))

        return retList

class DragAndDropExercise(forms.Form):
    exercise_id = forms.IntegerField(required=True, widget=forms.HiddenInput)
    bloat = forms.CharField(required = True,label="",widget=forms.HiddenInput)
    
    def clean_bloat(self):
        order = self.cleaned_data['bloat'].split('_')
        retDict = {}

        for word in order:
            num, img = word.split()
            img = img.split("|")
            retDict[num] = (img[0], img[1])

        return retDict
