from django import template

register = template.Library()

def eve_desc_filter(value):
    result = value[:150]
    result += "..."
    return result

register.filter('eve_desc_filter', eve_desc_filter)
