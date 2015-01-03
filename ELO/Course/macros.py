#coding: utf-8

## @file macros.py
#
#   Arquivo contendo todas as macros utilizadas no módulo de Cursos.

import ELO.locale.index as lang

from django.utils.encoding import force_unicode

## Macro responsável por armazenar a URL relativa dos templates de lições
LESSONS_URL = lambda x="": 'Course/lessons/' + str(x)

## Macro responsável por armazenar a URL relativa dos templates gerais do curso
GENERAL_URL = lambda x="": 'Course/general/' + str(x)

## Macro responsável por armazenar a URL relativa dos templates de exercícios
EXERCISES_URL = lambda x="": 'Course/exercises/' + str(x)

## Macro responsável por envolver o HTML fornecido por tags de <form>
FORM_WRAPPER = lambda x,y: '<form>' + str(x) + '<input type="hidden" name="csrfmiddlewaretoken" value="' + str(y) + '" /><input type="submit" value="' + force_unicode(lang.DICT['SUBMIT']) + '" /></form>'

## Macro responsável por mapear tipos de exercícios com seus respectivos ids 
class ExerciseType:
    MultipleChoice  = 1
    FillTheBlank    = 2
    CrossWords      = 3
    Unscramble      = 4
    DragAndDrop     = 5