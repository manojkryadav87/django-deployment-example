from atexit import register
from django import template

register = template.library()

@register.filter(name='cut')

def cut(value,arg):
    """
    This cits out all values of "arg" from the string!
    """
    return value.replace(arg,'')


#register.filter('cut',cut)