"""
Decorators are functions that takes another function and extends
the behavior of the latter function without explicitly modifying it.
You may want to read https://realpython.com/primer-on-python-decorators/
to learn more about decorators in Python.

We use the :py:func:`functools.wraps` decorator method to restore function name
and docstring.
"""
from functools import wraps


def view_decorator(func):
    """Decorator example."""

    @wraps(func)
    def wrap(request, *args, **kwargs):
        # What you want your decorator to do goes here typically...
        return func(request, *args, **kwargs)

    return wrap
