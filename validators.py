"""
Django validators for form and model fields.
They raise :py:exc:`ValidationError` if the input is invalid.

To use it, add the attribute ``validators=[validate_value]`` to the model field.

For more information on Django validators, see
https://docs.djangoproject.com/en/4.0/ref/validators/.
"""
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_value(value):
    """Validator for validating the value is present."""
    if not value:
        raise ValidationError(_("Not a valid value."), code="invalid-value")
