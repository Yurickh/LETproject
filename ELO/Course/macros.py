#coding: utf-8

## @file macros.py
#
#   Arquivo contendo todas as macros utilizadas no módulo de Cursos.

import ELO.locale.index as lang

from django.utils.encoding import force_unicode

## Macro responsável por mapear tipos de exercícios com seus respectivos ids 
class ExerciseType:

    MultipleChoice  = 1
    FillTheBlank    = 2
    CrossWords      = 3
    Unscramble      = 4
    DragAndDrop     = 5

## Macro responsável por armazenar a URL relativa dos templates de lições
LESSONS_URL = lambda x="": 'Course/lessons/' + str(x)

## Macro responsável por armazenar a URL relativa dos templates gerais do curso
GENERAL_URL = lambda x="": 'Course/general/' + str(x)

## Macro responsável por armazenar a URL relativa dos templates de exercícios
EXERCISES_URL = lambda x="": 'Course/exercises/' + str(x)

## Macro responsável por envolver um campo <input> com o código csrf
CSRF_WRAPPER = lambda x: \
    '<input type="hidden" name="csrfmiddlewaretoken" value="' + str(x) + '" />'

## Macro responsável por criar um botão de submissão
SUBMIT_WRAPPER = \
    '<input type="submit" value="'+force_unicode(lang.DICT['SUBMIT'])+'" />'

## Macro responsável por envolver o HTML fornecido por tags de <form>
FORM_WRAPPER = lambda x,y,z: \
    '<form>' + z[0] + " " + str(x) + " " + z[1] + CSRF_WRAPPER(y) + SUBMIT_WRAPPER + '</form>'

## Macro responsável por envolver o HTML fornecido por tags de <form>, já
#   deixando pronto para ser criado um exercício do tipo Drag'N'Drop
DND_WRAPPER = lambda x, y, z: \
    z[0] + '<div id="dnd_image"></div><br />' + z[1] + '<div id="dnd_holder"></div><br /><form>' + str(x) + CSRF_WRAPPER(y) + SUBMIT_WRAPPER + '</form>'
