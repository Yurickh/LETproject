from django.template import Library

register = Library()

@register.filter
def table_student(field):
	fields = ['NAME', 'MATRIC', 'EMAIL']
	return field in fields
