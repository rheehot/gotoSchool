from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='lookup')
def lookup(value, arg):
    return value[arg]