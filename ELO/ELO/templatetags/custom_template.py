from django.template import Library

register = Library()

@register.filter
def table_student(field):
	fields = ['NAME', 'MATRIC', 'EMAIL']
	return field in fields

@register.filter
def table_professor(field):
	fields = ['NAME', 'EMAIL']
	return field in fields

@register.filter
def table_course(field):
	fields = ['NAME', 'MATRIC', 'PROFESSOR']
	return field in fields
