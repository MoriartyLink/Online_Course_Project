from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiply the value by arg."""
    return float(value) * float(arg)