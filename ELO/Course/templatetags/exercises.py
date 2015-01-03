#coding: utf-8

from django import template

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

			print exercise_node

			return 'exercicio aqui :P'
			
		except template.VariableDoesNotExist:
			return ''