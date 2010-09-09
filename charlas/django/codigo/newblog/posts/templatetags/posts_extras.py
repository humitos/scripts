from django import template

register = template.Library()

@register.filter
def sayhello(value):
    return "Hello " + value
