# pylint: disable=invalid-name
"""
Custom Signals for the {{ app_name }} application.

See the Django documentation at
https://docs.djangoproject.com/en/4.0/topics/signals/ on how to send them.
"""
from django.dispatch import Signal


make_example = Signal()
"""Make example signal. Takes instance and user as arguments."""
