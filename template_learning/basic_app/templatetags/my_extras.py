from django import template

register= template.Library()

def mycut(value,arg):
    return value.replace(arg,' ')

register.filter('custom',mycut)
