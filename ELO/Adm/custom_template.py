from django.template import Library

register = Library()

@register.filter(name='not_None')
def not_None(arg): 
    return arg is not None

@register.filter(name='something')
def something(arg):
	return arg is True
