#coding: utf-8

from django import template

from Course.forms import MultipleChoiceExercise
from Course.macros import ExerciseType, FORM_WRAPPER

import ELO.locale.index as lang

register = template.Library()

@register.tag
def exercise(parser, token):
	try:
		tname = token.split_contents()
	except ValueError:
		exc_msg = lang.DICT['TEMPLATE_TAG_MA'] % token.contents.split()[0]
		raise template.TemplateSyntaxError(exc_msg)
	return ExerciseToken()

class ExerciseToken(template.Node):

	exercise = None

	def __init__(self, exercise):
		self.exercise = exercise

	def __init__(self): pass

	def render(self, context):
		try:
			if not exercise:
				exercise_node = context['exercise']
			else:
				exercise_node = self.exercise.render(context)

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

			return FORM_WRAPPER(exercise, exercise_node['csrf'])
			
		except template.VariableDoesNotExist:
			return ''