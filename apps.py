# pylint: disable=import-outside-toplevel
"""
App configs for the {{ app_name }} app.
Connects signal receivers.
See Also https://docs.djangoproject.com/en/4.0/ref/applications/.
"""
from django.apps import AppConfig


class {{ camel_case_app_name }}Config(AppConfig):
    """Default app config for {{ app_name }} app."""

    name = '{{ app_name }}'
    verbose_name = '{{ app_name }}'

    def ready(self):
        """Setup the signal receivers."""
        import {{ app_name }}.signal_receivers
