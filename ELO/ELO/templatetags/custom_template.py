from django.template import Library

register = Library()

@register.filter(name='not_None')
def not_None(arg): 
    return arg is not None

@register.filter
def table_student(field):
	fields = ['NAME', 'MATRIC', 'EMAIL']
	return field in fields
