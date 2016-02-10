"""
Custom managers and querysets for models for the {{ app_name }} app.
The managers are made from queryset classes with `as_manager()`
or `from_queryset()` methods to make them chainable.
See also https://docs.djangoproject.com/en/4.0/topics/db/managers/#creating-a-manager-with-queryset-methods.
"""
from django.db import models


class ModelQuerySet(models.QuerySet):
    """ModelQuerySet used as a manager for Model."""

    def with_number_of_replies(self):
        pass
