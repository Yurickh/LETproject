#coding: utf-8

from django import template

from Course.forms import MultipleChoiceExercise
from Course.macros import ExerciseType, FORM_WRAPPER

import ELO.locale.index as lang

register = template.Library()

@register.tag
def exercise(parser, token):
    try:
        ## {% exercise %} behaviour
        tname = token.split_contents()
        return ExerciseToken()
    except ValueError: pass

    try:
        ## {% exercise exer_name %} or {% exercise "enunciation" %} behaviour
        tname, tok = token.split_contents()
        return ExerciseToken(tok)
    except ValueError: pass

    exc_msg = lang.DICT['TEMPLATE_TAG_MA'] % token.contents.split()[0]

    try:
        ## {% exercise exer_name "enunciation" %} behaviour
        tname, exerciseName, formatString = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(exc_msg)
    else:
        if formatString[0]!=formatString[-1] or formatString not in ["'",'"']:
            raise template.TemplateSyntaxError(exc_msg)
        else:
            return ExerciseToken(exerciseName, formatString[1:-1])

class ExerciseToken(template.Node):

    exercise = None
    formatString = None

    def __init__(self, exercise, formatString):
        self.exercise = exercise
        self.formatString = formatString

    def __init__(self, token):
        if token[0] == token[-1] and token[0] in ["'", '"']:
            self.formatString = token[1:-1]
        else:
            self.exercise = token

    def __init__(self): pass

    def render(self, context):
        try:
            if not exercise:
                exercise_node = context['exercise']
            else:
                exercise_node = self.exercise.render(context)
        except template.VariableDoesNotExist:
            if not self.exercise[0] == self.exercise[-1] and\
               self.exercise[0] in ["'", '"']:
                    return ""
            else:
                enunciation = self.exercise[1:-1].split("%_")
                if len(enunciation) < 2:
                    enunciation.append("")
        else
            enunciation = ["",""]

        if exercise_node['type'] == ExerciseType.MultipleChoice:
            exercise = MultipleChoiceExercise()
            exercise.fields['options'].choices = exercise_node['options']

        elif exercise_node['type'] == ExerciseType.FillTheBlank:
            exercise = FillTheBlankExercise()

        elif exercise_node['type'] == ExerciseType.CrossWords:
            exercise = CrossWordsExercise()
            init_str = "_".join(exercise_node['words'])
            exercise.fields['bloat'].initial = init_str

        elif exercise_node['type'] == ExerciseType.Unscramble:
            exercise = UnscrambleExercise()
            init_str = " ".join(exercise_node['words'])
            exercise.fields['bloat'].initial = init_str

        elif exercise_node['type'] == ExerciseType.DragAndDrop:
            exercise = DragAndDropExercise()
            # something goes here, probably

        else:
            exercise = ''

        return FORM_WRAPPER(exercise, exercise_node['csrf'], enunciation)