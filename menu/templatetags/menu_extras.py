from django import template

register = template.Library()

@register.filter(name='minutestohours')
def minutestohours(value):
    return value / 60.0