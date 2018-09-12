# https://stackoverflow.com/questions/5827590/css-styling-in-django-forms?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

