"""
Custom Django templatetags and filters for the {{ app_name }} application.
For more information on custom Django template tags, see:
https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/.
"""
from django import template

register = template.Library()


@register.simple_tag
def bigger_than_four(value):
    """Returns a boolean based on if the value is bigger than four or not."""
    return int(value, 10) > 4
