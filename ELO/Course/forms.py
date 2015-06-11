#coding: utf-8

from django import forms
from ELO.BaseUnit import Id, PlainText

import ELO.locale.index as lang

class LessonForm(forms.Form):
    lesson_id = forms.IntegerField(required=True)
    slide_number = forms.IntegerField(required=True)

    def clean_lesson_id(self):
        return Id(self.cleaned_data['lesson_id'])

    def clean_slide_number(self):
        return Id(self.cleaned_data['slide_number'])

class ExerciseForm(forms.Form):
    exercise_id = forms.IntegerField(required=True, widget=forms.HiddenInput)
    options = forms.ChoiceField(widget  = forms.RadioSelect, required=False)
    blank   = forms.CharField(required=False)
    bloat   = forms.CharField(required=False)

    def clean_exercise_id(self):
        try:
            eid = Id(self.cleaned_data['exercise_id'])
        except ValueError:
            raise forms.ValidationError(lang.DICT['EXCEPTION_INV_ID'])
        return eid


def MultipleChoiceExercise(options):

    def clean_options(self):
        return self.cleaned_data['options'] #fazer tipo básico!

    ncfields = {  'options':  forms.ChoiceField(widget   = forms.RadioSelect, 
                                                required = True,
                                                label    = "",
                                                choices  = options,),
                'blank': None,
                'bloat': None,
                'clean_options': clean_options,
            }

    return type('MultipleChoiceExercise', (ExerciseForm,forms.BaseForm), ncfields)

class FillTheBlankExercise(ExerciseForm):
    blank = forms.CharField(required = True, label="")
    options = bloat = None

    def clean_blank(self):
        try:
            blank = PlainText(self.cleaned_data['blank'])
        except ValueError:
            raise forms.ValidationError(lang.DICT['EXCEPTION_INV_ANS'])

class UnscrambleExercise(ExerciseForm):
    bloat = forms.CharField(required = True, label="")
    options = blank = None

    def clean_bloat(self):
        return self.cleaned_data['bloat'].split() #fazer tipo básico!

class CrossWordExercise(ExerciseForm):
    bloat = forms.CharField(required = True, label="")
    options = blank = None

    def clean_bloat(self):
        wordList = self.cleaned_data['bloat'].split('_')
        retList = []

        for word in wordList:
            x,y,d,w = word.split()
            retList.append(" ".join([x,y,d,w]))

        return retList # fazer tipo básico!

class DragAndDropExercise(ExerciseForm):
    bloat = forms.CharField(required = True,label="",widget=forms.HiddenInput)
    options = blank = None
    
    def clean_bloat(self):
        order = self.cleaned_data['bloat'].split('_')
        retDict = {}

        for word in order:
            num, img = word.split()
            img = img.split("|")
            retDict[num] = (img[0], img[1])

        return retDict #fazer tipo básico!
