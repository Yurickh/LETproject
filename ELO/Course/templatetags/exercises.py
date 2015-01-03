#coding: utf-8

from django import template

from Course.forms import MultipleChoiceExercise
from Course.macros import ExerciseType, FORM_WRAPPER

import ELO.locale.index as lang

register = template.Library()

@register.tag
def exercise(parser, token):
	try:
		tname, exerc = token.split_contents()
	except ValueError:
		exc_msg = lang.DICT['TEMPLATE_TAG_MA'] % token.contents.split()[0]
		raise template.TemplateSyntaxError(exc_msg)
	return ExerciseToken(exerc)

class ExerciseToken(template.Node):
	
	def __init__(self, exercise_token):
		self.exercise_token = template.Variable(exercise_token)

	def render(self, context):
		try:
			exercise_node = self.exercise_token.resolve(context)

			if exercise_node['type'] == ExerciseType.MultipleChoice:
				exercise = MultipleChoiceExercise()
				exercise.fields['options'].choices = exercise_node['options']
			else:
				exercise = ''

			return FORM_WRAPPER(exercise, exercise_node['csrf'])
			
		except template.VariableDoesNotExist:
			return ''